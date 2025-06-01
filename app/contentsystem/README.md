# Viral Content Creation System

An advanced AI-powered system for creating viral video content across multiple platforms using specialized agents and optimization techniques.

## Features

### Content Creation Agents
- **Hook Creator Agent**: Creates compelling 5-10 second hooks
- **Shorts Script Agent**: Writes viral short-form video scripts (30-60 seconds)
- **Long Script Agent**: Creates engaging 3-5 minute video scripts
- **Title Optimization Agent**: Generates platform-specific viral titles
- **Description Agent**: Crafts optimized descriptions with strategic hashtags
- **Hashtag Strategy Agent**: Manages platform-specific hashtag strategies
- **Viral Techniques Agent**: Implements proven viral content techniques

### Platform Support
- TikTok (200+ hashtags)
- YouTube (25 strategic hashtags)
- Instagram (Trending and targeted hashtags)

### Optimization Features
- Platform-specific content formatting
- Hook generation and optimization
- Pattern interrupt implementation
- Retention strategy integration
- Hashtag optimization
- Title and description formatting

## Project Structure
```
agent_system/
├── README.md                 # Project documentation
├── requirements.txt          # Project dependencies
├── main.py                  # Core agent system implementation
├── database_manager.py      # Database operations handler
├── viral_techniques.py      # Viral content techniques library
├── platform_optimizer.py    # Platform-specific optimization
├── initial_hashtags.py      # Initial hashtag data
├── initialize_system.py     # System setup and testing
└── example_usage.py         # Usage examples and demonstrations
```

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure your Groq API key:
```bash
# Windows
set GROQ_API_KEY=your-api-key-here

# Unix/Linux/MacOS
export GROQ_API_KEY=your-api-key-here
```

3. Initialize the system:
```bash
python initialize_system.py
```

4. Run the application:
```bash
python main.py
```

## Usage

### Basic Usage
1. Launch the Gradio interface using `main.py`
2. Enter your video topic or concept
3. Get a complete viral content strategy including:
   - Hooks
   - Scripts
   - Titles
   - Descriptions
   - Hashtags
   - Implementation techniques

### Example Usage
Run `example_usage.py` to see demonstrations of:
- Short-form content creation
- Long-form content creation
- Educational content
- Trending topic content
- Viral technique implementation

## Components

### Main System (`main.py`)
- Coordinates multiple specialized agents
- Manages the Gradio interface
- Processes content requests
- Combines agent responses into strategies

### Database Manager (`database_manager.py`)
- Manages content storage and retrieval
- Tracks platform-specific hashtags
- Stores viral techniques and content metadata
- Provides trending hashtag analytics

### Viral Techniques (`viral_techniques.py`)
- Hook patterns library
- Pattern interrupts collection
- Retention strategies
- Psychological triggers
- Script templates
- Platform best practices

### Platform Optimizer (`platform_optimizer.py`)
- Platform-specific content formatting
- Title optimization
- Description formatting
- Script optimization
- Hook generation
- Pattern interrupt implementation

### Initial Hashtags (`initial_hashtags.py`)
- Platform-specific hashtag collections
- Trending hashtags
- Niche-specific tags
- Engagement-focused tags

### System Initialization (`initialize_system.py`)
- Database setup
- Data initialization
- System testing
- Configuration verification

## Content Creation Process

1. **Hook Creation**
   - Identify compelling moments
   - Create curiosity gaps
   - Implement emotional triggers

2. **Script Writing**
   - Short-form (30-60 seconds)
     - Fast-paced engagement
     - Pattern interrupts
     - Clear call-to-actions
   
   - Long-form (3-5 minutes)
     - Storytelling elements
     - Emotional peaks and valleys
     - Strategic pattern interrupts

3. **Platform Optimization**
   - TikTok
     - Short, punchy content
     - Trending sounds integration
     - Maximum hashtag utilization
   
   - YouTube
     - SEO optimization
     - Strategic timestamps
     - Engagement points
   
   - Instagram
     - Visual optimization
     - Strategic hashtag placement
     - Engagement triggers

4. **Content Enhancement**
   - Pattern interrupts
   - Psychological triggers
   - Retention strategies
   - Engagement prompts

## Best Practices

1. **Hook Creation**
   - Lead with shocking/interesting moments
   - Create curiosity gaps
   - Use emotional triggers
   - Keep it under 10 seconds

2. **Platform Optimization**
   - TikTok: Fast-paced, trend-focused
   - YouTube: SEO-optimized, value-driven
   - Instagram: Visually engaging, relatable

3. **Hashtag Strategy**
   - TikTok: 200+ strategic tags
   - YouTube: 25 searchable tags
   - Instagram: Mix of trending and niche

4. **Content Structure**
   - Hook → Value → Call-to-action
   - Pattern interrupts every 7-10 seconds
   - Clear storytelling arc
   - Strong emotional elements

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - feel free to use this code for your own projects!
