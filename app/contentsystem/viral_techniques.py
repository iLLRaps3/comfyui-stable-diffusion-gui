"""
Library of viral content techniques, patterns, and frameworks.
This file provides strategies and templates for creating viral content.
"""

from typing import Dict, List

class ViralTechniques:
    """Collection of viral content creation techniques and patterns."""
    
    @staticmethod
    def get_hook_patterns() -> Dict[str, str]:
        """Get proven hook patterns for video content."""
        return {
            "curiosity_gap": "Start with an incomplete story or surprising fact that creates curiosity",
            "shocking_statement": "Lead with a controversial or unexpected statement",
            "promise_pattern": "Make a bold promise about what viewers will learn/gain",
            "problem_solution": "Present a common problem and hint at your solution",
            "story_hook": "Begin with the most intense moment of your story",
            "statistic_hook": "Start with a surprising statistic or data point",
            "question_hook": "Ask a thought-provoking or relatable question",
            "mistake_revelation": "Reveal a common mistake people make",
            "secret_sharing": "Tease insider information or industry secrets",
            "time_sensitive": "Create urgency with time-sensitive information"
        }

    @staticmethod
    def get_pattern_interrupts() -> Dict[str, str]:
        """Get pattern interrupt techniques for maintaining viewer attention."""
        return {
            "visual_changes": "Sudden changes in camera angle, zoom, or scene",
            "audio_shifts": "Changes in music, sound effects, or voice tone",
            "text_overlay": "Adding sudden text animations or captions",
            "transition_effects": "Using creative transitions between segments",
            "emotion_switches": "Shifting between different emotional tones",
            "pace_changes": "Alternating between fast and slow pacing",
            "perspective_shifts": "Switching between different viewpoints",
            "format_breaks": "Mixing different content formats (talk, demo, etc.)",
            "unexpected_elements": "Including surprising or contrasting elements",
            "energy_variation": "Varying energy levels throughout the content"
        }

    @staticmethod
    def get_retention_strategies() -> Dict[str, str]:
        """Get strategies for maximizing viewer retention."""
        return {
            "open_loops": "Create multiple unresolved storylines throughout the content",
            "micro_cliffhangers": "End segments with mini-cliffhangers",
            "value_stacking": "Layer multiple benefits or insights throughout",
            "callback_references": "Reference earlier points to create coherence",
            "future_pacing": "Tease upcoming valuable information",
            "engagement_prompts": "Ask viewers questions or prompt interaction",
            "story_weaving": "Weave multiple story threads together",
            "anticipation_building": "Build anticipation for key revelations",
            "content_chunking": "Break content into digestible segments",
            "pattern_recognition": "Create recognizable patterns then break them"
        }

    @staticmethod
    def get_psychological_triggers() -> Dict[str, str]:
        """Get psychological triggers for engaging viewers."""
        return {
            "social_proof": "Show others' success or engagement",
            "scarcity": "Emphasize limited availability or exclusive information",
            "authority": "Demonstrate expertise or credibility",
            "reciprocity": "Provide value before asking for engagement",
            "commitment": "Get small commitments that lead to larger ones",
            "unity": "Create a sense of belonging or community",
            "loss_aversion": "Highlight what viewers might miss out on",
            "identity": "Appeal to viewers' self-image or aspirations",
            "curiosity": "Create knowledge gaps that need to be filled",
            "emotional_resonance": "Connect with viewers' emotions"
        }

    @staticmethod
    def get_script_templates() -> Dict[str, Dict[str, str]]:
        """Get templates for different types of viral videos."""
        return {
            "tutorial": {
                "hook": "Common mistake or pain point (5-10s)",
                "intro": "Quick credibility establishment (5-10s)",
                "steps": "Clear, actionable steps (30-60s)",
                "results": "Show before/after or benefits (10-15s)",
                "cta": "Clear call-to-action (5-10s)"
            },
            "story": {
                "hook": "Most intense moment (5-10s)",
                "context": "Quick background setup (10-15s)",
                "conflict": "Main challenge or obstacle (20-30s)",
                "resolution": "How it was overcome (15-20s)",
                "lesson": "Key takeaway or message (10-15s)"
            },
            "listicle": {
                "hook": "Best item or shocking fact (5-10s)",
                "setup": "What makes this list special (5-10s)",
                "items": "Rapid-fire list items (30-60s)",
                "bonus": "Unexpected extra value (10-15s)",
                "summary": "Quick recap and CTA (5-10s)"
            }
        }

    @staticmethod
    def get_engagement_prompts() -> List[str]:
        """Get prompts for driving viewer engagement."""
        return [
            "Comment below if you've experienced this...",
            "Let me know in the comments which tip was most helpful...",
            "Drop a 🔥 if you want a detailed video on...",
            "Share this with someone who needs to see this...",
            "Follow for more content like this...",
            "Save this for later when you need it...",
            "Tag someone who should know this...",
            "Double tap if you learned something new...",
            "Turn on notifications to see more...",
            "Duet this with your reaction..."
        ]

    @staticmethod
    def get_title_frameworks() -> Dict[str, List[str]]:
        """Get frameworks for creating viral titles."""
        return {
            "how_to": [
                "How I [achieved result] in [timeframe]",
                "How to [solve problem] (without [common solution])",
                "The REAL way to [achieve goal]",
                "Nobody talks about THIS way to [achieve result]"
            ],
            "listicle": [
                "X Things [group] Doesn't Want You to Know",
                "X [industry] Secrets That Will Change Everything",
                "X Ways to [achieve goal] (#X Will Shock You)",
                "I Tried X [methods/products] - Here's What Happened"
            ],
            "story": [
                "I Did [action] for X Days - SHOCKING RESULTS",
                "The Truth About [topic] That Nobody Tells You",
                "What Really Happens When You [action]",
                "From [starting point] to [end result] in X Days"
            ]
        }

    @staticmethod
    def get_viral_indicators() -> Dict[str, List[str]]:
        """Get indicators that suggest viral potential."""
        return {
            "content_elements": [
                "Strong emotional trigger",
                "Clear value proposition",
                "Relatable situation",
                "Novel information or approach",
                "Timing with trends"
            ],
            "technical_aspects": [
                "First 3 seconds hook",
                "Proper pacing",
                "High production value",
                "Clear audio",
                "Effective captions"
            ],
            "engagement_factors": [
                "Comment-worthy content",
                "Share-worthy value",
                "Save-worthy information",
                "Duet/Stitch potential",
                "Community involvement"
            ]
        }

    @staticmethod
    def get_platform_best_practices() -> Dict[str, Dict[str, List[str]]]:
        """Get platform-specific best practices."""
        return {
            "tiktok": {
                "duration": ["7-15 seconds for hooks", "30-60 seconds total"],
                "style": [
                    "Fast-paced editing",
                    "Multiple scene changes",
                    "Text overlay throughout",
                    "Trending sound integration"
                ],
                "optimization": [
                    "Vertical 9:16 format",
                    "Face visible in first frame",
                    "Trending music/sounds",
                    "Strategic hashtag placement"
                ]
            },
            "youtube": {
                "duration": ["15-30 second hook", "3-5 minutes for shorts"],
                "style": [
                    "Professional editing",
                    "Clear narrative structure",
                    "High-quality b-roll",
                    "Consistent branding"
                ],
                "optimization": [
                    "SEO-optimized titles",
                    "Custom thumbnails",
                    "End screens",
                    "Cards and chapters"
                ]
            },
            "instagram": {
                "duration": ["3-5 second hook", "30 seconds for reels"],
                "style": [
                    "Visually appealing content",
                    "Smooth transitions",
                    "On-screen text",
                    "Trending effects"
                ],
                "optimization": [
                    "High-quality visuals",
                    "Location tagging",
                    "Collaborative tags",
                    "Story highlights"
                ]
            }
        }
