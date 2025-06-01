"""
Platform-specific content optimization utilities.
This module handles formatting and optimization for different social media platforms.
"""

from typing import Dict, List, Optional
import re
from viral_techniques import ViralTechniques

class PlatformOptimizer:
    """Handles platform-specific content optimization and formatting."""

    def __init__(self):
        """Initialize the optimizer with viral techniques."""
        self.techniques = ViralTechniques()
        self.best_practices = self.techniques.get_platform_best_practices()

    def optimize_title(self, platform: str, title: str, hashtags: List[str]) -> str:
        """
        Optimize a title for a specific platform.
        
        Args:
            platform (str): Target platform
            title (str): Original title
            hashtags (List[str]): Available hashtags
            
        Returns:
            str: Optimized title
        """
        platform = platform.lower()
        
        if platform == 'tiktok':
            # TikTok: Short, punchy, with 3 relevant hashtags
            title = title[:50]  # TikTok title length limit
            selected_tags = self._select_best_hashtags(hashtags, 3)
            return f"{title} {' '.join(['#' + tag for tag in selected_tags])}"
            
        elif platform == 'youtube':
            # YouTube: SEO-optimized, longer format
            title = title[:100]  # YouTube title length limit
            selected_tags = self._select_best_hashtags(hashtags, 3)
            return f"{title} {' '.join(['#' + tag for tag in selected_tags])}"
            
        elif platform == 'instagram':
            # Instagram: Clean with strategic hashtags
            title = title[:125]  # Instagram caption preview limit
            selected_tags = self._select_best_hashtags(hashtags, 3)
            return f"{title}\n\n{' '.join(['#' + tag for tag in selected_tags])}"
            
        return title

    def optimize_description(self, platform: str, description: str, hashtags: List[str]) -> str:
        """
        Optimize a description for a specific platform.
        
        Args:
            platform (str): Target platform
            description (str): Original description
            hashtags (List[str]): Available hashtags
            
        Returns:
            str: Optimized description
        """
        platform = platform.lower()
        
        if platform == 'tiktok':
            # TikTok: Short description with many hashtags
            desc_limit = 300
            selected_tags = self._select_best_hashtags(hashtags, 20)  # TikTok allows many hashtags
            hashtag_str = ' '.join(['#' + tag for tag in selected_tags])
            main_desc = description[:desc_limit - len(hashtag_str) - 5]
            return f"{main_desc}\n\n{hashtag_str}"
            
        elif platform == 'youtube':
            # YouTube: Detailed description with timestamps and links
            selected_tags = self._select_best_hashtags(hashtags, 25)
            hashtag_str = ' '.join(['#' + tag for tag in selected_tags])
            return self._format_youtube_description(description, hashtag_str)
            
        elif platform == 'instagram':
            # Instagram: Balanced description with strategic hashtags
            selected_tags = self._select_best_hashtags(hashtags, 30)
            return self._format_instagram_caption(description, selected_tags)
            
        return description

    def optimize_script(self, platform: str, script: str, duration: int) -> str:
        """
        Optimize a script for a specific platform.
        
        Args:
            platform (str): Target platform
            script (str): Original script
            duration (int): Target duration in seconds
            
        Returns:
            str: Optimized script
        """
        platform = platform.lower()
        practices = self.best_practices.get(platform, {})
        
        # Add pattern interrupts based on platform
        if platform == 'tiktok':
            return self._optimize_tiktok_script(script, duration)
        elif platform == 'youtube':
            return self._optimize_youtube_script(script, duration)
        elif platform == 'instagram':
            return self._optimize_instagram_script(script, duration)
            
        return script

    def generate_hook(self, platform: str, content: str) -> str:
        """
        Generate a platform-specific hook from content.
        
        Args:
            platform (str): Target platform
            content (str): Main content to create hook from
            
        Returns:
            str: Optimized hook
        """
        hook_patterns = self.techniques.get_hook_patterns()
        platform_practices = self.best_practices.get(platform.lower(), {})
        
        # Extract key moments or statements
        key_moments = self._extract_key_moments(content)
        
        if platform.lower() == 'tiktok':
            # TikTok: Very short, shocking or curiosity-driven
            return self._create_tiktok_hook(key_moments)
        elif platform.lower() == 'youtube':
            # YouTube: Can be slightly longer, focus on value proposition
            return self._create_youtube_hook(key_moments)
        elif platform.lower() == 'instagram':
            # Instagram: Visual-first with strong opening line
            return self._create_instagram_hook(key_moments)
            
        return key_moments[0] if key_moments else ""

    def _select_best_hashtags(self, hashtags: List[str], count: int) -> List[str]:
        """Select the best hashtags based on relevance and engagement potential."""
        # In a real implementation, this would use engagement data and trends
        return hashtags[:count]

    def _format_youtube_description(self, description: str, hashtags: str) -> str:
        """Format a YouTube description with timestamps and sections."""
        template = f"""{description}

TIMESTAMPS:
00:00 - Introduction
{self._generate_timestamps(description)}

{hashtags}

FOLLOW ME ON SOCIAL MEDIA:
Instagram: @youraccount
TikTok: @youraccount
Twitter: @youraccount

#viral #trending #content"""
        return template

    def _format_instagram_caption(self, description: str, hashtags: List[str]) -> str:
        """Format an Instagram caption with strategic hashtag placement."""
        main_text = description[:2000]  # Instagram caption limit
        hashtag_groups = self._group_hashtags(hashtags)
        
        return f"""{main_text}

.
.
.

{' '.join(['#' + tag for tag in hashtag_groups['primary']])}

{' '.join(['#' + tag for tag in hashtag_groups['secondary']])}"""

    def _optimize_tiktok_script(self, script: str, duration: int) -> str:
        """Optimize a script for TikTok."""
        # Add pattern interrupts every 5-7 seconds
        interrupt_interval = 6  # seconds
        num_interrupts = duration // interrupt_interval
        
        optimized_script = "HOOK (0-3 seconds):\n[Hook goes here]\n\n"
        optimized_script += "MAIN CONTENT:\n"
        
        paragraphs = script.split('\n\n')
        for i, paragraph in enumerate(paragraphs):
            if i < num_interrupts:
                optimized_script += f"{paragraph}\n[Pattern Interrupt: {self._get_pattern_interrupt()}]\n\n"
            else:
                optimized_script += f"{paragraph}\n\n"
                
        optimized_script += "\nCALL TO ACTION:\n[Strong CTA goes here]"
        return optimized_script

    def _optimize_youtube_script(self, script: str, duration: int) -> str:
        """Optimize a script for YouTube."""
        # Add pattern interrupts every 45-60 seconds
        interrupt_interval = 45  # seconds
        num_interrupts = duration // interrupt_interval
        
        optimized_script = "HOOK (0-15 seconds):\n[Hook goes here]\n\n"
        optimized_script += "INTRO (15-30 seconds):\n[Quick intro and value proposition]\n\n"
        optimized_script += "MAIN CONTENT:\n"
        
        paragraphs = script.split('\n\n')
        for i, paragraph in enumerate(paragraphs):
            if i < num_interrupts:
                optimized_script += f"{paragraph}\n[Pattern Interrupt: {self._get_pattern_interrupt()}]\n\n"
            else:
                optimized_script += f"{paragraph}\n\n"
                
        optimized_script += "\nCALL TO ACTION:\n[Multi-part CTA with subscription reminder]"
        return optimized_script

    def _optimize_instagram_script(self, script: str, duration: int) -> str:
        """Optimize a script for Instagram."""
        # Add pattern interrupts every 8-10 seconds
        interrupt_interval = 8  # seconds
        num_interrupts = duration // interrupt_interval
        
        optimized_script = "HOOK (0-3 seconds):\n[Visual hook goes here]\n\n"
        optimized_script += "MAIN CONTENT:\n"
        
        paragraphs = script.split('\n\n')
        for i, paragraph in enumerate(paragraphs):
            if i < num_interrupts:
                optimized_script += f"{paragraph}\n[Visual Pattern Interrupt: {self._get_pattern_interrupt()}]\n\n"
            else:
                optimized_script += f"{paragraph}\n\n"
                
        optimized_script += "\nCALL TO ACTION:\n[Platform-specific CTA]"
        return optimized_script

    def _get_pattern_interrupt(self) -> str:
        """Get a random pattern interrupt technique."""
        interrupts = self.techniques.get_pattern_interrupts()
        return list(interrupts.values())[0]  # In real implementation, would be random

    def _extract_key_moments(self, content: str) -> List[str]:
        """Extract potential hook-worthy moments from content."""
        # In a real implementation, this would use NLP to identify compelling moments
        sentences = content.split('.')
        return [s.strip() for s in sentences if len(s.strip()) > 20][:5]

    def _create_tiktok_hook(self, key_moments: List[str]) -> str:
        """Create a TikTok-optimized hook."""
        if not key_moments:
            return ""
        return f"🤯 {key_moments[0][:50]}..."

    def _create_youtube_hook(self, key_moments: List[str]) -> str:
        """Create a YouTube-optimized hook."""
        if not key_moments:
            return ""
        return f"In this video, you'll discover {key_moments[0][:100]}..."

    def _create_instagram_hook(self, key_moments: List[str]) -> str:
        """Create an Instagram-optimized hook."""
        if not key_moments:
            return ""
        return f"✨ {key_moments[0][:80]}..."

    def _generate_timestamps(self, description: str) -> str:
        """Generate fake timestamps for demonstration."""
        return """02:30 - Main Topic
05:45 - Key Points
08:15 - Examples
12:00 - Tips & Tricks
15:30 - Conclusion"""

    def _group_hashtags(self, hashtags: List[str]) -> Dict[str, List[str]]:
        """Group hashtags by priority."""
        return {
            'primary': hashtags[:10],
            'secondary': hashtags[10:]
        }
