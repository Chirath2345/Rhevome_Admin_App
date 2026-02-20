import configparser
import os
from typing import Optional


class ConfigReader:
    """Configuration reader for Playwright tests"""
    
    def __init__(self, config_file_path: Optional[str] = None):
        if config_file_path is None:
            # Default to config/config.ini in the new project structure
            config_file_path = os.path.join(
                os.path.dirname(__file__), 
                "..", 
                "config", 
                "config.ini"
            )
        
        self.config = configparser.RawConfigParser()
        self.config.read(config_file_path)
    
    def get_application_url(self) -> str:
        """Get base URL from config"""
        return self.config.get('common data', 'baseURL')
    
    def get_email(self) -> str:
        """Get email from config"""
        return self.config.get('common data', 'email')
    
    def get_secondary_email(self) -> str:
        """Get secondary email from config"""
        return self.config.get('common data', 'secondaryemail')
    
    def get_invite_email(self, email) -> str:
        """Get secondary email from config"""
        return self.config.get('common data', email)
    
    def get_password(self) -> str:
        """Get password from config"""
        return self.config.get('common data', 'password')
    
    def get_new_password(self) -> str:
        """Get new password from config"""
        return self.config.get('common data', 'newpassword')
    
    def get_username(self) -> str:
        """Get username from config"""
        return self.config.get('common data', 'UserName')
    
    def get(self, section: str, key: str, fallback: Optional[str] = None) -> str:
        """Get a config value by section and key"""
        try:
            return self.config.get(section, key)
        except:
            return fallback if fallback else ""
        
    def get_google_email(self) -> str:
        """Get google email from config"""
        return self.config.get('common data', 'googleemail')
    
    def get_google_password(self) -> str:
        """Get google password from config"""
        return self.config.get('common data', 'googlepassword')

