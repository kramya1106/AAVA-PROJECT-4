"""
Page Object for User Registration Page
This page object represents the user registration page with all form fields.
"""

from playwright.sync_api import Page
from pages.base_page_object import BasePageObject


class RegistrationPage(BasePageObject):
    """Page object for the user registration page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.elements.registration_form = "form, [class*='registration'], [class*='register'], [id*='registration']"
        self.elements.username_input = "input[name='username'], input[id='username'], input[placeholder*='username' i]"
        self.elements.email_input = "input[type='email'], input[name='email'], input[id='email']"
        self.elements.password_input = "input[type='password'][name='password'], input[type='password'][id='password']"
        self.elements.confirm_password_input = "input[type='password'][name*='confirm'], input[type='password'][id*='confirm']"
        self.elements.first_name_input = "input[name='firstName'], input[name='first_name'], input[id='firstName'], input[placeholder*='first name' i]"
        self.elements.last_name_input = "input[name='lastName'], input[name='last_name'], input[id='lastName'], input[placeholder*='last name' i]"
        self.elements.submit_button = "button[type='submit'], button:has-text('Submit'), button:has-text('Register'), button:has-text('Sign Up')"
        self.elements.processing_indicator = "[class*='spinner'], [class*='loading'], [class*='processing']"
        self.elements.username_error_message = "[class*='error']:near(input[name='username'])"
        self.elements.email_error_message = "[class*='error']:near(input[type='email'])"
        self.elements.password_error_message = "[class*='error']:near(input[type='password'][name='password'])"
        self.elements.confirm_password_error_message = "[class*='error']:near(input[type='password'][name*='confirm'])"
        self.elements.first_name_error_message = "[class*='error']:near(input[name='firstName'])"
        self.elements.last_name_error_message = "[class*='error']:near(input[name='lastName'])"

    def is_registration_page_displayed(self):
        """Verify registration page and form are displayed."""
        return self.registration_form.is_visible()

    def enter_username(self, username: str):
        """Clear and enter username in username field."""
        self.username_input.clear()
        self.username_input.fill(username)

    def enter_email(self, email: str):
        """Clear and enter email in email field."""
        self.email_input.clear()
        self.email_input.fill(email)

    def enter_password(self, password: str):
        """Clear and enter password in password field."""
        self.password_input.clear()
        self.password_input.fill(password)

    def enter_confirm_password(self, confirm_password: str):
        """Clear and enter confirm password in confirm password field."""
        self.confirm_password_input.clear()
        self.confirm_password_input.fill(confirm_password)

    def enter_first_name(self, first_name: str):
        """Clear and enter first name in first name field."""
        self.first_name_input.clear()
        self.first_name_input.fill(first_name)

    def enter_last_name(self, last_name: str):
        """Clear and enter last name in last name field."""
        self.last_name_input.clear()
        self.last_name_input.fill(last_name)

    def click_submit_button(self):
        """Click submit button to submit registration form."""
        self.submit_button.click()

    def fill_registration_form(self, username: str, email: str, password: str, 
                               confirm_password: str, first_name: str, last_name: str):
        """Composite method to fill all registration form fields."""
        self.enter_username(username)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)

    def is_processing_indicator_visible(self):
        """Verify processing indicator is shown after form submission."""
        return self.processing_indicator.is_visible()

    def get_field_value(self, field_name: str):
        """Get the value of a specified form field."""
        field_map = {
            "username": self.username_input,
            "email": self.email_input,
            "first_name": self.first_name_input,
            "last_name": self.last_name_input
        }
        field = field_map.get(field_name)
        if field:
            return field.input_value()
        return None

    def is_field_error_visible(self, field_name: str):
        """Check if error message is visible for specified field."""
        error_map = {
            "username": self.username_error_message,
            "email": self.email_error_message,
            "password": self.password_error_message,
            "confirm_password": self.confirm_password_error_message,
            "first_name": self.first_name_error_message,
            "last_name": self.last_name_error_message
        }
        error_element = error_map.get(field_name)
        if error_element:
            return error_element.is_visible()
        return False
