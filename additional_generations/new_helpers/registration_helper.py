"""
Helper for User Registration Flows
This helper orchestrates the complete user registration workflow.
"""

from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.success_page import SuccessPage
from core.settings import framework_logger


class RegistrationHelper:
    """Helper for user registration related flows."""

    @staticmethod
    def navigate_to_registration_page(page: Page):
        """Navigate from home page to registration page by clicking Register button."""
        home_page = HomePage(page)
        home_page.navigate()
        page.wait_for_load_state("networkidle", timeout=30000)
        expect(home_page.home_page_container).to_be_visible(timeout=30000)
        
        home_page.click_register_button()
        page.wait_for_load_state("domcontentloaded", timeout=30000)
        
        registration_page = RegistrationPage(page)
        expect(registration_page.registration_form).to_be_visible(timeout=30000)
        
        framework_logger.info("Navigated to registration page successfully")

    @staticmethod
    def complete_registration(page: Page, username: str, email: str, password: str, 
                            first_name: str, last_name: str):
        """Complete entire registration flow: fill form and submit."""
        registration_page = RegistrationPage(page)
        
        # Fill all form fields
        registration_page.fill_registration_form(
            username=username,
            email=email,
            password=password,
            confirm_password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        framework_logger.info(f"Registration form filled with username={username}, email={email}")
        
        # Submit form
        registration_page.click_submit_button()
        expect(registration_page.processing_indicator).to_be_visible(timeout=15000)
        
        framework_logger.info("Registration form submitted successfully")

    @staticmethod
    def verify_registration_success(page: Page, expected_message: str = "Registration successful"):
        """Verify registration completed successfully with expected success message."""
        success_page = SuccessPage(page)
        
        expect(success_page.success_message).to_be_visible(timeout=30000)
        expect(success_page.success_message).to_contain_text(expected_message, timeout=30000)
        expect(success_page.success_page_container).to_be_visible(timeout=30000)
        
        framework_logger.info(f"Registration success verified with message: {expected_message}")
        return True

    @staticmethod
    def full_registration_flow(page: Page, username: str, email: str, password: str,
                              first_name: str, last_name: str, 
                              expected_success_message: str = "Registration successful"):
        """Execute complete registration flow from home page to success verification."""
        RegistrationHelper.navigate_to_registration_page(page)
        RegistrationHelper.complete_registration(page, username, email, password, first_name, last_name)
        RegistrationHelper.verify_registration_success(page, expected_success_message)
        
        framework_logger.info("Full registration flow completed successfully")
