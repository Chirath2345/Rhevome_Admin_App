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

        # --- Sidebar Navigation Elements ---
        self.nav_dashboard_overview = page.get_by_role("button", name="Dashboard Overview")
        self.nav_order_management = page.get_by_role("button", name="Kit Fulfillment Kit")
        
        # Customer Care Group
        self.nav_customer_care_dropdown = page.get_by_role("button", name="Customer Care Manage")
        self.nav_customers = page.get_by_role("button", name="Customers Manage customers")
        self.nav_reports = page.get_by_role("button", name="Reports View reports")
        
        # Laboratory Group
        self.nav_laboratory_dropdown = page.get_by_role("button", name="Laboratory Lab operations")
        self.nav_lab_upload = page.get_by_role("button", name="Lab Upload Upload results")
        self.nav_ai_analysis = page.get_by_role("button", name="AI Analysis Generate reports")
        self.nav_ai_job_queue = page.get_by_role("button", name="AI Job Queue Monitor analysis")
        self.nav_three_day_reports = page.get_by_role("button", name="3-Day Reports Track daily")
        self.nav_qa_dashboard = page.get_by_role("button", name="QA Dashboard 8 Quality control")
        
        # Administration Group
        self.nav_administration_dropdown = page.get_by_role("button", name="Administration System admin")
        self.nav_user_management = page.get_by_role("button", name="User Management Manage users")
        self.nav_role_management = page.get_by_role("button", name="Role Management Manage roles")
        
        # Other Options
        self.nav_perplexity_articles = page.get_by_role("button", name="Perplexity Articles Review")
        self.nav_pdf_vector_upload = page.get_by_role("button", name="PDF Vector Upload Upload PDFs")
        self.nav_settings = page.get_by_role("button", name="Settings System config")
        self.nav_wiki = page.get_by_role("button", name="Wiki User guide & docs")

        # Notification Icon 
        self.notification_btn = page.get_by_role("button", name="Notifications")
        self.notification_panel = page.get_by_label("", exact=True)

        #Theme toggle
        self.theme_btn = page.get_by_role("button", name="🌙")
        self.theme_to_light_btn = page.get_by_role("button", name="🌞")
        self.dark_option = page.get_by_role("menuitem", name="Dark")
        self.light_option = page.get_by_role("menuitem", name="Light")

        self.profile_btn = page.get_by_role("button", name=re.compile(r"Administrator", re.I))
        self.profile_menu = page.get_by_role("menu", name=re.compile(r"Chamika J", re.I))

        # Profile Dropdown Elements
        self.profile_dropdown_trigger = page.get_by_role("banner").get_by_role("button", name=re.compile(r"Administrator", re.I))
        self.menu_admin_badge = page.get_by_text("Administrator", exact=True).first
        self.menu_user_email = page.get_by_text("chamika@ceydigital.com")
        self.menu_profile_settings = page.get_by_role("menuitem", name="Profile Settings")
        self.menu_notifications = page.get_by_role("menuitem", name=re.compile(r"Notifications", re.I))
        self.menu_help_support = page.get_by_role("menuitem", name="Help & Support")
        self.menu_sign_out = page.get_by_role("menuitem", name="Sign Out")

        # Profile Settings Elements
        self.profile_settings_title = page.get_by_text("Profile Settings", exact=True).first
        self.profile_settings_title_area = page.locator("div").filter(has_text=re.compile(r"Profile SettingsManage your", re.I)).first

        # Notifications link text
        self.menu_notifications_link = page.get_by_role("menuitem", name=re.compile(r"Notifications", re.I))
        self.notifications_page_header = page.get_by_role("heading", name="Notifications")

        # Help & Support link text
        self.menu_help_support_link = page.get_by_role("menuitem", name="Help & Support")
        self.help_page_header = page.get_by_role("heading", name=re.compile(r"Help|Support", re.I))

        self.menu_sign_out_link = page.get_by_role("menuitem", name="Sign Out")

        # Page load overview
        self.dashboard_overview_container = page.locator("div").filter(has_text=re.compile(r"DashboardWelcome.*Customer Segments Overview", re.I)).first

 #========================================================================================

    #------ Actions---------
    def open_notifications(self):
        """
        Clicks the notification icon.
        """
        self.notification_btn.click()
    
    def toggle_theme(self):
        if self.theme_to_dark_btn.count() > 0:
            self.theme_to_dark_btn.click()
        elif self.theme_to_light_btn.count() > 0:
            self.theme_to_light_btn.click()
    
    def open_profile_menu(self):
        self.profile_btn.click()

    def verify_profile_menu_visible(self):
        expect(self.profile_menu).to_be_visible()
    
    def select_profile_settings(self):
        self.profile_dropdown_trigger.click()
        self.menu_profile_settings.click()
    
    def select_notifications_from_profile(self):
        self.profile_dropdown_trigger.click() 
        self.menu_notifications_link.click()
    
    def select_help_support_from_profile(self):
        self.profile_dropdown_trigger.click()
        self.menu_help_support_link.click()
    
    def sign_out(self):
        self.profile_dropdown_trigger.click()
        self.menu_sign_out_link.click()