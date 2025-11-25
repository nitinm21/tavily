"""
Mock traditional search API (like Google, Bing, SerpAPI)

This simulates what traditional search APIs return:
- URLs
- Short snippets (meta descriptions)
- NO extracted full content

To get the full content, you'd need to:
1. Scrape each URL
2. Extract main content
3. Clean HTML
4. Handle errors
"""

class TraditionalSearchMock:
    """
    Simulates traditional search API behavior.
    In a real scenario, this would call Google Custom Search API or similar.
    """

    def __init__(self):
        pass

    def search(self, query, max_results=5):
        """
        Simulate a traditional search API response

        Returns only URLs and short snippets (like meta descriptions),
        NOT full extracted content - that's the key difference from Tavily.
        """

        # These are mock results that simulate what traditional search returns
        # In reality, you'd call an actual API here
        mock_results = self._generate_mock_results(query, max_results)

        return {
            'query': query,
            'results': mock_results,
            'total_results': len(mock_results)
        }

    def _generate_mock_results(self, query, max_results):
        """
        Generate mock results that simulate traditional search API behavior.

        Traditional APIs return:
        - Title
        - URL
        - Short snippet/description (typically meta description, ~160 chars)
        - NO full content extraction
        """

        # This simulates typical search results for any query
        # In a real implementation, this would be actual API data
        mock_templates = [
            {
                'title': f'{query.title()} - Comprehensive Guide',
                'url': f'https://example.com/guide/{query.replace(" ", "-")}',
                'snippet': f'Learn about {query} in this comprehensive guide. Discover the best practices, tips, and techniques for understanding {query}...'
            },
            {
                'title': f'Understanding {query.title()}: A Complete Overview',
                'url': f'https://docs.example.org/{query.replace(" ", "-")}',
                'snippet': f'Everything you need to know about {query}. This article covers the fundamentals, advanced concepts, and practical applications...'
            },
            {
                'title': f'{query.title()} Explained - Tutorial',
                'url': f'https://tutorial.site/{query.replace(" ", "/")}',
                'snippet': f'A step-by-step tutorial on {query}. Perfect for beginners and advanced users alike. Includes examples and best practices...'
            },
            {
                'title': f'Latest News and Updates on {query.title()}',
                'url': f'https://news.example.com/topics/{query.replace(" ", "-")}',
                'snippet': f'Stay up to date with the latest developments in {query}. Recent articles, announcements, and industry insights...'
            },
            {
                'title': f'{query.title()} - Wikipedia',
                'url': f'https://wikipedia.org/wiki/{query.replace(" ", "_")}',
                'snippet': f'{query.title()} refers to... From Wikipedia, the free encyclopedia. This article needs additional citations for verification...'
            }
        ]

        return mock_templates[:max_results]

    def get_snippet_length(self, results):
        """Get total length of all snippets"""
        total = 0
        for result in results.get('results', []):
            total += len(result.get('snippet', ''))
        return total

    def get_result_urls(self, results):
        """Extract URLs from results"""
        return [r.get('url', '') for r in results.get('results', [])]


class TraditionalSearchNote:
    """
    Helper class to explain the traditional search workflow
    """

    @staticmethod
    def get_workflow_steps():
        return [
            "1. Call search API (Google, Bing, SerpAPI)",
            "2. Get URLs and short snippets",
            "3. For each URL, you need to:",
            "   - Scrape the page (requests, selenium)",
            "   - Parse HTML (BeautifulSoup, lxml)",
            "   - Extract main content (custom logic)",
            "   - Clean and format text",
            "   - Handle errors (404s, timeouts, paywalls)",
            "4. Filter and rank extracted content",
            "5. Optimize for LLM context window",
            "6. Finally get RAG-ready content"
        ]

    @staticmethod
    def get_problems():
        return [
            "Multiple API calls required",
            "Complex scraping logic needed",
            "Error handling for each website",
            "Content extraction varies by site",
            "High latency (serial scraping)",
            "Maintenance burden (site changes)",
            "Rate limiting concerns",
            "Extra infrastructure needed"
        ]
