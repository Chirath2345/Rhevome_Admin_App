from playwright.sync_api import Page, expect
import re

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        
        # --- Header & Global Elements ---
        self.rhevome_logo = page.get_by_role("heading", name="Rhevome")
        self.sidebar_toggle = page.get_by_role("button").first
        self.page_title = page.get_by_role("banner").get_by_role("heading", name="Dashboard")
        self.welcome_msg = page.get_by_text("Welcome Chamika J")
        self.notification_bell = page.get_by_role("button", name="Notifications")
        self.theme_toggle = page.get_by_role("button", name="🌙")
        self.user_profile_btn = page.get_by_role("button", name="CJ Chamika J Administrator")
        
        # --- Filters & Actions ---
        self.date_filter = page.get_by_role("button", name="Last 30 Days")
        self.export_btn = page.get_by_role("button", name="Export")
        
        # --- Summary Cards & Indicators ---
        self.activation_rate = page.get_by_text("Activation Rate87.5%")
        self.completion_rate = page.get_by_text("Completion Rate0.0%")
        self.total_customers_card = page.get_by_text("Total CustomersPurchased a kit")
        self.active_customers_header = page.get_by_role("heading", name="Active Customers")
        
        # --- Lifecycle Values ---
        self.order_placed_val = page.get_by_text("Order Placed")
        self.kit_shipped_val = page.get_by_text("Kit Shipped")
        self.kit_activated_val = page.get_by_text("Kit ActivatedQuestionnaire pending0")
        self.questionnaire_completed_val = page.get_by_text("Questionnaire CompletedAwaiting results7")
        self.progress_bar = page.get_by_role("progressbar").nth(1)
        
        # --- Recent Reports Section ---
        self.reports_section = page.locator("div").filter(has_text=re.compile(r"^Recent Reports"))
        self.filter_btn = page.get_by_role("button", name="Filter")
        self.empty_reports_msg = page.get_by_text("No recent reports found")
        
        # --- Quick Actions Cards ---
        self.quick_actions_header = page.get_by_text("Quick Actions9 actions")
        self.view_reports_card = page.get_by_role("button", name="View Reports Browse all")
        self.manage_users_card = page.get_by_role("button", name="Manage Users Add or edit users")
        self.system_settings_card = page.get_by_role("button", name="System Settings Configure")
        self.view_customers_card = page.get_by_role("button", name="View Customers Manage")
        self.ai_analysis_card = page.get_by_role("button", name="AI Analysis Generate AI")
        self.upload_lab_card = page.get_by_role("button", name="Upload Lab Results Upload new")
        self.qa_dashboard_card = page.get_by_role("button", name="QA Dashboard Review and")
        self.ai_jobs_card = page.get_by_role("button", name="AI Jobs Queue Monitor AI")