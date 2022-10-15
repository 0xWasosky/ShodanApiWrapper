import requests


class Shodan:
    def __init__(self, api_key: str) -> None:
        """
        An unofficial API wrapper for : https://www.shodan.io/ made by Wassoky
        """
        self.key = api_key

    def Host(self, ip: str):
        self.ip = ip
        url = f"https://api.shodan.io/shodan/host/{self.ip}?key={self.key}"

        host_response = requests.get(url).json()

        return host_response

    def HostCount(self, CountQuery: str, CountFacets: str):
        self.CountQury = CountQuery
        self.CountFacets = CountFacets
        url = f"https://api.shodan.io/shodan/host/count?key={self.key}&query={self.CountQury}&facets={self.CountFacets}"

        host_count_response = requests.get(url).json()

        return host_count_response

    def HostSearch(self, SearchQuery: str, SearchFacets):
        self.SearchQuery = SearchQuery
        self.SearchFacets = SearchFacets
        url = f"https://api.shodan.io/shodan/host/search?key={self.key}&query={self.SearchQuery}&facets={self.SearchFacets}"

        host_search_response = requests.get(url).json()

        return host_search_response

    def HostFacets(self):
        url = f"https://api.shodan.io/shodan/host/search/facets?key={self.key}"

        return requests.get(url).json()

    def HostFilters(self):
        url = f"https://api.shodan.io/shodan/host/search/filters?key={self.key}"

        return requests.get(url).json()


class ShodanScanning:
    def __init__(self, api_key: str) -> None:
        """
        An unofficial API wrapper for : https://www.shodan.io/ made by Wassoky
        """
        self.key = api_key

    def Ports(self):
        url = f"https://api.shodan.io/shodan/ports?key={self.key}"

        return requests.get(url).json()

    def Protocols(self):
        url = f"https://api.shodan.io/shodan/protocols?key={self.key}"

        return requests.get(url).json()

class ShodanDNS:
    def __init__(self, api_key: str) -> None:
        """
        An unofficial API wrapper for : https://www.shodan.io/ made by Wassoky
        """
        self.key = api_key
    
    def Domain(self, domain: str):
        "Exemple: google.com"
        self.domain = domain
        url = f"https://api.shodan.io/dns/domain/{self.domain}?key={self.key}"

        dns_domain_response = requests.get(url).json()

        return dns_domain_response
    
    def Resolve(self, domanins: str):
        "Exemple: exemple.com,exempl.org"
        self.domains = domanins
        url = f"https://api.shodan.io/dns/resolve?hostnames={self.domains}&key={self.key}"

        dns_resolve_response = requests.get(url).json()

        return dns_resolve_response
    
    def Reverse(self, ips: str):
        "Exemple: 142.250.180.174"
        self.ips = ips
        url = f"https://api.shodan.io/dns/reverse?ips={ips}&key={self.key}"

        dns_reverse_response = requests.get(url).json()

        return dns_reverse_response

class ShodanUtility:
    def __init__(self, api_key: str) -> None:
        """
        An unofficial API wrapper for : https://www.shodan.io/ made by Wassoky
        """
        self.key = api_key
    
    def HttpHeaders(self):
        "Shows the HTTP headers that your client sends when connecting to a webserver. -> Shodan docs"
        url = f"https://api.shodan.io/tools/httpheaders?key={self.key}"

        return requests.get(url).json()
    
    def MyIp(self):
        "Return your ip"
        url = f"https://api.shodan.io/tools/myip?key={self.key}"

        return requests.get(url).json()
