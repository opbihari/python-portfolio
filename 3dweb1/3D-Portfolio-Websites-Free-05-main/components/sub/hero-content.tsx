"use client";

import { motion } from "framer-motion";
import Link from "next/link";

export const HeroContent = () => {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 1 }}
      className="flex flex-row items-center justify-center px-20 mt-40 w-full z-[20] h-screen"
    >
      <div className="w-full flex justify-center items-center">
        <div className="orbit-container animate-revolve">
          {/* Black Hole 1: Skills */}
          <Link href="#skills" className="blackhole-orb orb-1">
            <div className="w-full h-full flex justify-center items-center animate-counter-revolve">
              <video
                autoPlay
                muted
                loop
                className="orb-video"
              >
                <source src="/videos/blackhole.webm" type="video/webm" />
              </video>
              <span className="orb-text">Skills</span>
            </div>
          </Link>

          {/* Black Hole 2: About me */}
          <Link href="#about-me" className="blackhole-orb orb-2">
            <div className="w-full h-full flex justify-center items-center animate-counter-revolve">
              <video
                autoPlay
                muted
                loop
                className="orb-video"
              >
                <source src="/videos/blackhole.webm" type="video/webm" />
              </video>
              <span className="orb-text text-center">About me</span>
            </div>
          </Link>

          {/* Black Hole 3: Projects */}
          <Link href="#projects" className="blackhole-orb orb-3">
            <div className="w-full h-full flex justify-center items-center animate-counter-revolve">
              <video
                autoPlay
                muted
                loop
                className="orb-video"
              >
                <source src="/videos/blackhole.webm" type="video/webm" />
              </video>
              <span className="orb-text">Projects</span>
            </div>
          </Link>
        </div>
      </div>
    </motion.div>
  );
};
