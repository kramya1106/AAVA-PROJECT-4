"""
Test Case ID: TC_REG_001
Title: Verify User Registration with Valid Data
Description: This test case verifies that a new user can successfully register on the 
application by providing valid registration details including username, email, password, 
and personal information. The test validates form field interactions, data validation, 
submission process, and successful account creation confirmation.
"""

import traceback
import pytest
from core.playwright_manager import PlaywrightManager
from core.settings import framework_logger
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.success_page import SuccessPage
from playwright.sync_api import expect
import test_flows_common.test_flows_common as common
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@pytest.mark.usefixtures("main_execution")
def test_tc_reg_001_user_registration(stage_callback, tc_tracer, reporter):
    tcid = "TC_REG_001"
    current_step = "Step 0"
    current_validation = "Initialization"

    try:
        common.setup()
        
        # Generate unique test data
        timestamp = common.generate_timestamp()
        username = f"testuser_{timestamp}"
        email = common.generate_tenant_email()
        password = "Test@1234"
        first_name = "John"
        last_name = "Doe"
        
        framework_logger.info(f"[{tcid}] Test data generated: username={username}, email={email}")

        # ── Step 1: Navigate to the application URL ──
        current_step = "Step 1"
        current_validation = "Application home page is displayed"

        with PlaywrightManager() as page:
            home_page = HomePage(page)
            home_page.navigate()
            page.wait_for_load_state("networkidle", timeout=30000)
            
            expect(home_page.home_page_container).to_be_visible(timeout=30000)
            stage_callback("step1_home_page", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 1: Navigated to application home page")
            reporter.validate(True, f"[{tcid}] Step 1: Navigated to application home page")

            # ── Step 2: Click on 'Register' button ──
            current_step = "Step 2"
            current_validation = "Registration page is displayed with registration form"

            home_page.register_button.click()
            page.wait_for_load_state("domcontentloaded", timeout=30000)
            
            registration_page = RegistrationPage(page)
            expect(registration_page.registration_form).to_be_visible(timeout=30000)
            stage_callback("step2_registration_page", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 2: Registration page displayed with form")
            reporter.validate(True, f"[{tcid}] Step 2: Registration page displayed with form")

            # ── Step 3: Enter valid username in 'Username' field ──
            current_step = "Step 3"
            current_validation = "Username is entered successfully"

            registration_page.username_input.clear()
            registration_page.username_input.fill(username)
            expect(registration_page.username_input).to_have_value(username, timeout=10000)
            framework_logger.info(f"[{tcid}] Step 3: Username entered successfully")
            reporter.validate(True, f"[{tcid}] Step 3: Username entered successfully")

            # ── Step 4: Enter valid email in 'Email' field ──
            current_step = "Step 4"
            current_validation = "Email is entered successfully"

            registration_page.email_input.clear()
            registration_page.email_input.fill(email)
            expect(registration_page.email_input).to_have_value(email, timeout=10000)
            framework_logger.info(f"[{tcid}] Step 4: Email entered successfully")
            reporter.validate(True, f"[{tcid}] Step 4: Email entered successfully")

            # ── Step 5: Enter valid password in 'Password' field ──
            current_step = "Step 5"
            current_validation = "Password is entered successfully and masked"

            registration_page.password_input.clear()
            registration_page.password_input.fill(password)
            expect(registration_page.password_input).to_have_attribute("type", "password", timeout=10000)
            framework_logger.info(f"[{tcid}] Step 5: Password entered and masked successfully")
            reporter.validate(True, f"[{tcid}] Step 5: Password entered and masked successfully")

            # ── Step 6: Enter valid password in 'Confirm Password' field ──
            current_step = "Step 6"
            current_validation = "Confirm password is entered successfully and matches password"

            registration_page.confirm_password_input.clear()
            registration_page.confirm_password_input.fill(password)
            expect(registration_page.confirm_password_input).to_have_attribute("type", "password", timeout=10000)
            framework_logger.info(f"[{tcid}] Step 6: Confirm password entered successfully")
            reporter.validate(True, f"[{tcid}] Step 6: Confirm password entered successfully")

            # ── Step 7: Enter valid first name in 'First Name' field ──
            current_step = "Step 7"
            current_validation = "First name is entered successfully"

            registration_page.first_name_input.clear()
            registration_page.first_name_input.fill(first_name)
            expect(registration_page.first_name_input).to_have_value(first_name, timeout=10000)
            framework_logger.info(f"[{tcid}] Step 7: First name entered successfully")
            reporter.validate(True, f"[{tcid}] Step 7: First name entered successfully")

            # ── Step 8: Enter valid last name in 'Last Name' field ──
            current_step = "Step 8"
            current_validation = "Last name is entered successfully"

            registration_page.last_name_input.clear()
            registration_page.last_name_input.fill(last_name)
            expect(registration_page.last_name_input).to_have_value(last_name, timeout=10000)
            framework_logger.info(f"[{tcid}] Step 8: Last name entered successfully")
            reporter.validate(True, f"[{tcid}] Step 8: Last name entered successfully")

            # ── Step 9: Click on 'Submit' button ──
            current_step = "Step 9"
            current_validation = "Registration is submitted and processing indicator is shown"

            registration_page.submit_button.click()
            expect(registration_page.processing_indicator).to_be_visible(timeout=15000)
            stage_callback("step9_form_submitted", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 9: Registration form submitted with processing indicator")
            reporter.validate(True, f"[{tcid}] Step 9: Registration form submitted with processing indicator")

            # ── Step 10: Verify success message is displayed ──
            current_step = "Step 10"
            current_validation = "Success message 'Registration successful' is displayed and user is redirected to success page"

            success_page = SuccessPage(page)
            expect(success_page.success_message).to_be_visible(timeout=30000)
            expect(success_page.success_message).to_contain_text("Registration successful", timeout=30000)
            expect(success_page.success_page_container).to_be_visible(timeout=30000)
            stage_callback("step10_success_page", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 10: Registration successful - success message displayed")
            reporter.validate(True, f"[{tcid}] Step 10: Registration successful - success message displayed")

    except Exception as e:
        framework_logger.error(
            f"[{tcid}] Test failed at {current_step} — {current_validation}: "
            f"{e}\n{traceback.format_exc()}"
        )
        reporter.validate(False, f"[{tcid}] FAIL at {current_step} — {current_validation}: {str(e)}")
        raise
