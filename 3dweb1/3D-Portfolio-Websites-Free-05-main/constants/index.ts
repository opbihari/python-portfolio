import { FaYoutube, FaFacebook } from "react-icons/fa";
import {
  RxDiscordLogo,
  RxGithubLogo,
  RxInstagramLogo,
  RxTwitterLogo,
  RxLinkedinLogo,
} from "react-icons/rx";

export const SKILL_DATA = [
  {
    skill_name: "Python",
    image: "python.svg",
    width: 80,
    height: 80,
  },
  {
    skill_name: "HTML",
    image: "html.png",
    width: 80,
    height: 80,
  },
  {
    skill_name: "CSS",
    image: "css.png",
    width: 80,
    height: 80,
  },
  {
    skill_name: "JSON",
    image: "json.svg",
    width: 80,
    height: 80,
  },
  {
    skill_name: "C",
    image: "c.svg",
    width: 80,
    height: 80,
  },
  {
    skill_name: "C++",
    image: "cpp.svg",
    width: 80,
    height: 80,
  },
] as const;

export const SOCIALS = [
  {
    name: "Instagram",
    icon: RxInstagramLogo,
    link: "https://instagram.com",
  },
  {
    name: "Facebook",
    icon: FaFacebook,
    link: "https://facebook.com",
  },
  {
    name: "Twitter",
    icon: RxTwitterLogo,
    link: "https://twitter.com",
  },
] as const;

export const FRONTEND_SKILL = [] as const;

export const BACKEND_SKILL = [] as const;

export const FULLSTACK_SKILL = [] as const;

export const OTHER_SKILL = [] as const;

export const PROJECTS = [
  {
    title: "Python AI Code Assistant",
    description: "A robust Flask-based backend API that integrates with multiple LLM providers (Google Gemini, OpenAI GPT-4, Anthropic Claude). It exposes endpoints to automatically generate Python code snippets from natural language prompts, explain code logic, and suggest refactoring improvements.",
    image: "/projects/project-1.png",
    link: "https://github.com",
  },
  {
    title: "DDoS Detector & Firewall Simulator",
    description: "A security-focused project that analyzes server logs to identify potential Distributed Denial of Service (DDoS) attacks. It processes raw text logs, counts IP requests, and flags suspicious activity.",
    image: "/projects/project-2.png",
    link: "https://github.com",
  },
  {
    title: "IP Blacklist Checker",
    description: "An interactive security tool that checks IP addresses against a simulated threat intelligence database. It provides real-time alerts based on threat levels and previous blocks.",
    image: "/projects/project-3.png",
    link: "https://github.com",
  },
  {
    title: "Web Scraping Data Extractor",
    description: "A web scraper built using Python's requests and BeautifulSoup libraries. It connects to a target website, parses the HTML DOM to extract specific data elements, and saves the structured output into a CSV file.",
    image: "/projects/project-4.png",
    link: "https://github.com",
  },
  {
    title: "Contact Management System",
    description: "A fully functional CLI-based contact management system that allows users to add, view, and delete contacts with persistent data storage utilizing CSV files.",
    image: "/projects/project-5.png",
    link: "https://github.com",
  },
  {
    title: "Online Book Store Inventory",
    description: "An interactive bookstore inventory management application. It handles tasks such as adding new books, tracking unique genres, updating information for existing books, and removing sold books.",
    image: "/projects/project-6.png",
    link: "https://github.com",
  },
] as const;

export const FOOTER_DATA = [
  {
    title: "Community",
    data: [
      {
        name: "YouTube",
        icon: FaYoutube,
        link: "https://youtube.com",
      },
      {
        name: "GitHub",
        icon: RxGithubLogo,
        link: "https://github.com",
      },
      {
        name: "Discord",
        icon: RxDiscordLogo,
        link: "https://discord.com",
      },
    ],
  },
  {
    title: "Social Media",
    data: [
      {
        name: "Instagram",
        icon: RxInstagramLogo,
        link: "https://instagram.com",
      },
      {
        name: "Twitter",
        icon: RxTwitterLogo,
        link: "https://twitter.com",
      },
      {
        name: "Linkedin",
        icon: RxLinkedinLogo,
        link: "https://linkedin.com",
      },
    ],
  },
  {
    title: "About",
    data: [
      {
        name: "Become Sponsor",
        icon: null,
        link: "https://youtube.com",
      },
      {
        name: "Learning about me",
        icon: null,
        link: "https://example.com",
      },
      {
        name: "Contact Me",
        icon: null,
        link: "mailto:contact@example.com",
      },
    ],
  },
] as const;

export const NAV_LINKS = [
  {
    title: "About me",
    link: "#about-me",
  },
  {
    title: "Skills",
    link: "#skills",
  },
  {
    title: "Projects",
    link: "#projects",
  },
] as const;

export const LINKS = {
  sourceCode: "https://github.com",
};
