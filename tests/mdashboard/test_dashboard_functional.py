from playwright.sync_api import Page, expect
from pages.login.login_page import LoginPage
from pages.mdashboard.dashboard_page import DashboardPage

class TestAdminDashboard:
    def test_tc_01_verify_ui_elements_in_admin_dashboard(self, page: Page):
        """
        TC_01: Verify UI elements in Admin Dashboard
        """
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)
        login_page.navigate()
        login_page.login_with_remember_me("chamika@ceydigital.com", "Qwer@#12345")
        page.wait_for_load_state("networkidle")
        # Logo and Header
        expect(dashboard_page.rhevome_logo).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.sidebar_toggle).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.page_title).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.welcome_msg).to_be_visible()
        page.wait_for_timeout(500)
        
        # Global Icons
        expect(dashboard_page.notification_bell).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.theme_toggle).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.user_profile_btn).to_be_visible()
        page.wait_for_timeout(500)

        # Filters
        expect(dashboard_page.date_filter).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.export_btn).to_be_visible()
        page.wait_for_timeout(500)

        # Summary Metrics
        expect(dashboard_page.activation_rate).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.completion_rate).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.total_customers_card).to_be_visible()
        page.wait_for_timeout(500)

        # Lifecycle Progress
        expect(dashboard_page.order_placed_val).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.kit_shipped_val).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.kit_activated_val).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.questionnaire_completed_val).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.progress_bar).to_be_visible()
        page.wait_for_timeout(500)

        # Reports Section
        expect(dashboard_page.filter_btn).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.empty_reports_msg).to_be_visible()
        page.wait_for_timeout(500)

        # Quick Actions
        expect(dashboard_page.quick_actions_header).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.view_reports_card).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.manage_users_card).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.system_settings_card).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.ai_analysis_card).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.ai_jobs_card).to_be_visible()
        page.wait_for_timeout(500)

    def test_tc_02_verify_sidebar_ui_elements(self, page: Page):
        """
        TC_02: Verify UI elements in Sidebar with helper texts
        """
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)
        login_page.navigate()
        login_page.login_with_remember_me("chamika@ceydigital.com", "Qwer@#12345")
        page.wait_for_load_state("networkidle")
        expect(dashboard_page.nav_dashboard_overview).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_order_management).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_customer_care_dropdown).to_be_visible()
        page.wait_for_timeout(500) 
        expect(dashboard_page.nav_customers).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_reports).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_laboratory_dropdown).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_lab_upload).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_ai_analysis).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_ai_job_queue).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_three_day_reports).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_qa_dashboard).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_administration_dropdown).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_user_management).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_role_management).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_perplexity_articles).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_pdf_vector_upload).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_settings).to_be_visible()
        page.wait_for_timeout(500)
        expect(dashboard_page.nav_wiki).to_be_visible()