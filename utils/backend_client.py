import requests
from typing import Dict, List, Optional, Tuple
import os
from dotenv import load_dotenv

load_dotenv()

class BackendClient:
    
    def __init__(self, base_url: Optional[str] = None):
        self.base_url = base_url or os.getenv('BACKEND_URL', 'https://shiv06-backend-app.hf.space')
        self.session = requests.Session()
        self.timeout = 30
    
    def analyze_product(self, 
                       image_bytes: bytes,
                       dietary_needs: List[str],
                       image_filename: str = "product_image.jpg") -> Dict:
        url = f"{self.base_url}/api/analyze"
        
        files = {
            'image': (image_filename, image_bytes, 'image/jpeg')
        }
        
        data = {
            'dietary_needs': ','.join(dietary_needs)
        }
        
        try:
            response = self.session.post(url, files=files, data=data, timeout=self.timeout, verify=False)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Analyze product error: {str(e)}")
            raise Exception(f"Backend request failed: {str(e)}")
    
    def extract_text_from_image(self, image_bytes: bytes) -> Tuple[str, float]:
        url = f"{self.base_url}/api/extract-text"
        
        files = {
            'image': ('image.jpg', image_bytes, 'image/jpeg')
        }
        
        try:
            response = self.session.post(url, files=files, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('text', ''), data.get('confidence', 0.0)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Text extraction failed: {str(e)}")
    
    def search_product(self, barcode: str) -> Optional[Dict]:
        url = f"{self.base_url}/api/search-product"
        
        params = {
            'barcode': barcode
        }
        
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Product search failed: {str(e)}")
    
    def get_allergens(self, ingredients: List[str]) -> Dict[str, bool]:
        url = f"{self.base_url}/api/allergens"
        
        payload = {
            'ingredients': ingredients
        }
        
        try:
            response = self.session.post(url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Allergen detection failed: {str(e)}")
    
    def classify_additive(self, additive_code: str) -> Optional[Dict]:
        url = f"{self.base_url}/api/additive"
        
        params = {
            'code': additive_code
        }
        
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Additive classification failed: {str(e)}")
    
    def classify_dietary(self, 
                        ingredients: List[str],
                        dietary_category: str) -> Dict:
        url = f"{self.base_url}/api/classify-dietary"
        
        payload = {
            'ingredients': ingredients,
            'category': dietary_category
        }
        
        try:
            response = self.session.post(url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Dietary classification failed: {str(e)}")
    
    def health_check(self) -> bool:
        url = f"{self.base_url}/health"
        
        try:
            response = self.session.get(url, timeout=5, verify=False)
            print(f"Health check response: {response.status_code}")
            return response.status_code == 200
        except requests.exceptions.RequestException as e:
            print(f"Health check error: {str(e)}")
            return False
