import Sidebar from '@/components/Sidebar.component';
import MainContent from '@/components/MainContent.component';

export default function Home() {
  return (
    <main className="flex flex-row w-screen h-screen">
      <Sidebar />
      <MainContent />
    </main>
  );
}
