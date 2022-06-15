import requests

from .settings import BEVIGIL_API_URL
from .exceptions import APIError, InvalidAPIKeyError


class BeVigil:

    def __init__(self, api_key):
        self.api_key = api_key.strip()
        self._session = requests.Session()
        self.bevigil_api_url = BEVIGIL_API_URL

    def getWordlistFromPackage(self, package_id):
        """
        Returns wordlist created from package
        
        Parameters:
        name : package_id
        type : str

        Returns:
        name : wordlist
        type : dict
        """
        return self._request(endpoint=f"/api/{package_id}/wordlist/")

    def getHostsFromPackage(self, package_id):
        """
        Returns hosts associated with package
        
        Parameters:
        name : package_id
        type : str

        Returns:
        name : hosts
        type : dict
        """
        return self._request(endpoint=f"/api/{package_id}/hosts/")

    def getS3bucketsFromPackage(self, package_id):
        """
        Returns S3 buckets associated with package
        
        Parameters:
        name : package_id
        type : str

        Returns:
        name : S3_buckets
        type : dict
        """
        return self._request(endpoint=f"/api/{package_id}/S3-buckets/")

    def getPackagesFromDomain(self, domain):
        """
        Returns packages associated with the domain
        
        Parameters:
        name : domain
        type : str

        Returns:
        name : Packages
        type : dict
        """
        return self._request(endpoint=f"/api/{domain}/apps/")

    def getPackagesFromSubdomain(self, subdomain):
        """
        Returns packages associated with the Subdomain
        
        Parameters:
        name : subdomain
        type : str

        Returns:
        name : Packages
        type : dict
        """
        return self._request(f"/api/{subdomain}/apps/")

    def getParamsFromPackage(self, package_id):
        """
        Returns parameters associated with the Package ID
        
        Parameters:
        name : package_id
        type : str

        Returns:
        name : Parameters
        type : dict
        """
        return self._request(f"/api/{package_id}/params/")

    def getSubdomainsFromDomain(self, domain):
        """
        Returns Subdomains associated with a domain
        
        Parameters:
        name : domain
        type : str

        Returns:
        name : Subdomains
        type : dict
        """
        return self._request(f"/api/{domain}/subdomains/")

    def getUrlsFromDomain(self, domain):
        """
        Returns URLs associated with a domain

        Parameters:
        name : domain
        type : str

        Returns:
        name : URLs
        type : dict
        """
        return self._request(f"/api/{domain}/urls/")

    def getS3bucketsFromKeyword(self, keyword):
        """
        Returns S3 buckets data associated with the keyword

        Parameters:
        name : keyword
        type : str

        Returns:
        name : S3 buckets data
        type : dict
        """
        return self._request(f"/api/{keyword}/S3-keyword/")

    def validateKey(self):
        """
        Checks whether the API key is valid

        Returns:
        type : bool
        True when key is valid otherwise False
        """
        api_response = self._request(f"/api/keycheck/?token={self.api_key}")
        return api_response["valid"]

    def _request(self, endpoint, method="get"):
        """
        Internal function to send HTTP requests to API server and retrieve contents
        """

        # Constructing the function URL
        function_url = f"{self.bevigil_api_url}{endpoint}"

        # Adding API key in headers
        headers = {
            "X-Access-Token": self.api_key,
            "Accept": "application/json"
        }
        try:
            if method.lower() == "get":
                api_response = self._session.get(function_url, headers=headers)
            elif method.lower() == "post":
                api_response = self._session.post(function_url, headers=headers)
        except Exception:
            raise APIError("Unable to connect to BeVigil API")

        # Check if the API key was valid
        if api_response.status_code == 401:
            raise InvalidAPIKeyError("Invalid API Key")

        # Try parsing the JSON response
        try:
            json_data = api_response.json()
        except Exception:
            raise APIError("Unable to parse JSON response")

        # If any other error occurs
        if api_response.status_code == 400:
            if "detail" in json_data:
                raise APIError(json_data["detail"])
            else:
                raise APIError("Unexpected Error Occurred")

        return json_data
