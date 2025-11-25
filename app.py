from flask import Flask, render_template, request, jsonify
from config import Config
from utils.tavily_client import TavilySearchWrapper
from utils.traditional_search import TraditionalSearchMock, TraditionalSearchNote
from utils.metrics import RAGMetrics

app = Flask(__name__)
app.config.from_object(Config)

# Initialize search clients
tavily_client = TavilySearchWrapper()
traditional_client = TraditionalSearchMock()
metrics_calculator = RAGMetrics()


@app.route('/')
def index():
    """Main page with search form"""
    return render_template('index.html')


@app.route('/compare', methods=['POST'])
def compare():
    """
    Handle search comparison request

    Executes both Tavily and Traditional search,
    calculates metrics, and returns comparison data
    """
    query = request.form.get('query', '').strip()

    if not query:
        return jsonify({'error': 'Please enter a search query'}), 400

    max_results = int(request.form.get('max_results', Config.DEFAULT_MAX_RESULTS))

    try:
        # Execute both searches
        tavily_results = tavily_client.search(query, max_results)
        traditional_results = traditional_client.search(query, max_results)

        # Check for Tavily API errors
        if 'error' in tavily_results:
            return jsonify({
                'error': f'Tavily API Error: {tavily_results["error"]}'
            }), 500

        # Calculate metrics for both
        tavily_metrics = metrics_calculator.calculate_tavily_metrics(tavily_results)
        traditional_metrics = metrics_calculator.calculate_traditional_metrics(traditional_results)

        # Generate comparison insights
        comparison = metrics_calculator.compare_metrics(tavily_metrics, traditional_metrics)

        # Get workflow explanations
        traditional_workflow = TraditionalSearchNote.get_workflow_steps()
        traditional_problems = TraditionalSearchNote.get_problems()

        # Prepare response
        response = {
            'query': query,
            'tavily': {
                'results': tavily_results,
                'metrics': tavily_metrics
            },
            'traditional': {
                'results': traditional_results,
                'metrics': traditional_metrics,
                'workflow': traditional_workflow,
                'problems': traditional_problems
            },
            'comparison': comparison
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'tavily_api_configured': bool(Config.TAVILY_API_KEY)
    })


if __name__ == '__main__':
    app.run(
        debug=Config.FLASK_DEBUG,
        host='0.0.0.0',
        port=8080
    )
