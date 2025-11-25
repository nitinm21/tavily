from tavily import TavilyClient
from config import Config

class TavilySearchWrapper:
    """Wrapper for Tavily Search API"""

    def __init__(self):
        self.client = TavilyClient(api_key=Config.TAVILY_API_KEY)

    def search(self, query, max_results=5):
        """
        Execute a search using Tavily API

        Args:
            query: Search query string
            max_results: Maximum number of results to return

        Returns:
            Dictionary containing search results and metadata
        """
        try:
            response = self.client.search(
                query=query,
                max_results=max_results,
                search_depth="advanced",  # Get more comprehensive results
                include_answer=True,  # Get AI-generated answer
                include_raw_content=False,  # We want extracted content, not raw HTML
                include_images=False  # Not needed for Phase 1
            )

            # Extract and format the results
            formatted_results = {
                'query': query,
                'answer': response.get('answer', ''),
                'results': [],
                'raw_response': response
            }

            for result in response.get('results', []):
                formatted_results['results'].append({
                    'title': result.get('title', 'No title'),
                    'url': result.get('url', ''),
                    'content': result.get('content', ''),  # This is the extracted, clean content
                    'score': result.get('score', 0),
                    'raw_content': result.get('raw_content', '')
                })

            return formatted_results

        except Exception as e:
            return {
                'error': str(e),
                'query': query,
                'results': []
            }

    def get_extracted_content_length(self, results):
        """Get total length of extracted content"""
        total = 0
        for result in results.get('results', []):
            total += len(result.get('content', ''))
        return total

    def get_result_urls(self, results):
        """Extract URLs from results"""
        return [r.get('url', '') for r in results.get('results', [])]
