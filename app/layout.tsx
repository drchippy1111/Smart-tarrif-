import './globals.css' // Make sure Tailwind or your global styles are included
import { ReactNode } from 'react'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Smart Tarrif App',
  description: 'Optimize and analyze tariff plans with real-time monitoring and AI-powered predictions.',
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <head />
      <body className={`${inter.className} bg-gray-100 text-gray-900 min-h-screen`}>
        <header className="bg-blue-700 text-white p-4 shadow-md">
          <div className="container mx-auto text-xl font-bold">Smart Tarrif</div>
        </header>

        <main className="container mx-auto p-4">
          {children}
        </main>

        <footer className="bg-blue-800 text-white text-center p-4 mt-10">
          © {new Date().getFullYear()} Smart Tarrif — All rights reserved.
        </footer>
      </body>
    </html>
  )
}
