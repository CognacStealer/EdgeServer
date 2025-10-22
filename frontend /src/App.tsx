import { useState } from "react";
import { LoginPage } from "./components/LoginPage";
import { DashboardLayout } from "./components/DashboardLayout";
import { WorkspacePage } from "./components/WorkspacePage";
import { FineTunePage } from "./components/FineTunePage";
import { MyModelsPage } from "./components/MyModelsPage";
import { SettingsPage } from "./components/SettingsPage";

export default function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [currentPage, setCurrentPage] = useState("workspace");
  const [apiKey, setApiKey] = useState("");

  // Handle login from LoginPage
  const handleLogin = (key: string) => {
    setApiKey(key);
    setIsAuthenticated(true);
  };

  // Handle logout from DashboardLayout
  const handleLogout = () => {
    setIsAuthenticated(false);
    setApiKey("");
    setCurrentPage("workspace");
  };

  // Dynamically render page components
  const renderPage = () => {
    switch (currentPage) {
      case "workspace":
        return <WorkspacePage apiKey={apiKey} />;
      case "finetune":
        return <FineTunePage apiKey={apiKey} />;
      case "models":
        return <MyModelsPage apiKey={apiKey} />;
      case "settings":
        return <SettingsPage apiKey={apiKey} />;
      default:
        return <WorkspacePage apiKey={apiKey} />;
    }
  };

  // If not logged in, show login page
  if (!isAuthenticated) {
    return <LoginPage onLogin={handleLogin} />;
  }

  // If logged in, show dashboard and current page
  return (
    <DashboardLayout
      currentPage={currentPage}
      onNavigate={setCurrentPage}
      onLogout={handleLogout}
    >
      {renderPage()}
    </DashboardLayout>
  );
}
