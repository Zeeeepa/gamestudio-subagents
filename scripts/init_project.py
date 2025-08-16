#!/usr/bin/env python3
"""
Game Studio Project Initializer
Creates project structure and configures agents for game development

Author: Tuna Pamir (https://github.com/pamirtuna)
Project: Game Studio Sub-Agents
License: MIT
"""

import os
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from agent_customizer import AgentCustomizer


class ProjectInitializer:
    def __init__(self):
        self.base_path = Path("projects")
        self.project_config = {}
        
    def create_project_structure(self, project_name, engine="Godot"):
        """Create the complete project folder structure"""
        project_path = self.base_path / project_name.lower().replace(" ", "-")
        
        # Ensure base projects directory exists
        self.base_path.mkdir(exist_ok=True)
        
        # Engine-specific directory structure
        if engine == "Unity":
            directories = self.get_unity_structure()
        elif engine == "Unreal":
            directories = self.get_unreal_structure()
        else:  # Godot default
            directories = self.get_godot_structure()
        
        # Common project directories
        common_directories = [
            "documentation/design/systems",
            "documentation/design/mechanics",
            "documentation/design/content",
            "documentation/art/concepts",
            "documentation/art/assets",
            "documentation/art/style-guides",
            "documentation/technical/architecture",
            "documentation/technical/api-docs",
            "documentation/technical/performance",
            "documentation/production/milestones",
            "documentation/production/retrospectives",
            "documentation/production/reports",
            "resources/references",
            "resources/market-research",
            "resources/competitor-analysis",
            "qa/test-plans",
            "qa/bug-reports",
            "qa/playtesting",
            "qa/performance-logs",
            "builds/alpha",
            "builds/beta",
            "builds/release"
        ]
        
        # Combine engine-specific and common directories
        all_directories = directories + common_directories
        
        for directory in all_directories:
            (project_path / directory).mkdir(parents=True, exist_ok=True)
            
        return project_path
    
    def get_godot_structure(self):
        """Godot-specific folder structure"""
        return [
            "source/scenes",
            "source/scripts", 
            "source/assets/sprites",
            "source/assets/models",
            "source/assets/audio",
            "source/assets/ui",
            "source/assets/shaders",
            "source/assets/fonts",
            "source/autoload",
            "source/addons"
        ]
    
    def get_unity_structure(self):
        """Unity-specific folder structure"""
        return [
            "source/Assets/Scripts",
            "source/Assets/Scenes", 
            "source/Assets/Prefabs",
            "source/Assets/Materials",
            "source/Assets/Textures",
            "source/Assets/Models",
            "source/Assets/Audio",
            "source/Assets/Animations",
            "source/Assets/Shaders",
            "source/Assets/StreamingAssets",
            "source/Assets/Editor",
            "source/Assets/Resources",
            "source/Assets/Plugins",
            "source/Packages",
            "source/ProjectSettings"
        ]
    
    def get_unreal_structure(self):
        """Unreal Engine-specific folder structure"""
        return [
            "source/Content/Blueprints",
            "source/Content/Maps",
            "source/Content/Materials", 
            "source/Content/Meshes",
            "source/Content/Textures",
            "source/Content/Audio",
            "source/Content/Animations",
            "source/Content/UI",
            "source/Content/Particles",
            "source/Content/Characters",
            "source/Source/Public",
            "source/Source/Private",
            "source/Plugins",
            "source/Config"
        ]
    
    def create_initial_files(self, project_path, config):
        """Create initial project files"""
        
        # Project configuration
        config_file = project_path / "project-config.json"
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        # Game Design Document template
        gdd_file = project_path / "documentation/design/gdd.md"
        gdd_content = f"""# {config['project']['name']} - Game Design Document

## Overview
**Concept**: {config['project']['concept']}
**Genre**: {config['project']['genre']}
**Platform**: {config['project']['platform']}
**Target Audience**: {config['project']['audience']}

## Design Pillars
1. [Core Pillar 1]
2. [Core Pillar 2]
3. [Core Pillar 3]

## Core Gameplay Loop
[Describe the 30-second loop]

## Game Systems
[To be filled by Sr Game Designer]

## Content Specifications
[To be filled by Mid Game Designer]

## Technical Requirements
**Engine**: {config['project']['engine']}
**Performance Targets**: {config['metrics']['performance_target']}

## Art Direction
[To be filled by Sr Game Artist]

## UI/UX Design
[To be filled by UI/UX Agent]

## Audio Design
[Placeholder for audio specifications]

## Monetization Strategy
{config['project'].get('monetization', 'Not Applicable')}

## Success Metrics
- [Metric 1]
- [Metric 2]
- [Metric 3]
"""
        with open(gdd_file, 'w') as f:
            f.write(gdd_content)
        
        # README for source
        readme_file = project_path / "source/README.md"
        readme_content = f"""# {config['project']['name']} - Source Code

## Engine: {config['project']['engine']}

## Project Structure
- `/assets` - All game assets (art, audio, etc.)
- `/scripts` - Game logic and systems
- `/scenes` - Game scenes/levels
- `/prefabs` - Reusable game objects

## Setup Instructions
1. [Engine-specific setup steps]
2. [Dependencies installation]
3. [Build configuration]

## Development Guidelines
- Follow the coding standards in `/documentation/technical/`
- All commits must pass QA validation
- Use semantic versioning for releases

## Active Agents
{', '.join(config['team']['active_agents'])}

## Current Phase
{config['project'].get('phase', 'Initialization')}
"""
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        
        # Timeline
        timeline_file = project_path / "documentation/production/timeline.md"
        timeline_content = f"""# {config['project']['name']} - Production Timeline

## Project Timeline: {config['project']['timeline']}

## Milestones
"""
        for milestone in config['milestones']:
            timeline_content += f"""
### {milestone['name']} - {milestone['target_date']}
**Deliverables**:
"""
            for deliverable in milestone['deliverables']:
                timeline_content += f"- {deliverable}\n"
            
            timeline_content += "\n**Success Criteria**:\n"
            for criteria in milestone['success_criteria']:
                timeline_content += f"- {criteria}\n"
        
        with open(timeline_file, 'w') as f:
            f.write(timeline_content)
            
        # Create .gitignore
        gitignore_file = project_path / ".gitignore"
        gitignore_content = """# Builds
builds/
*.exe
*.app
*.apk

# Temp files
*.tmp
*.temp
.cache/

# IDE
.vscode/
.idea/
*.suo
*.user

# OS
.DS_Store
Thumbs.db

# Engine specific
.godot/
.import/
Library/
Temp/
Build/

# Logs
*.log
logs/
"""
        with open(gitignore_file, 'w') as f:
            f.write(gitignore_content)
        
        # Create engine-specific files
        engine = config['project']['engine']
        self.create_engine_files(project_path, engine)
    
    def create_engine_files(self, project_path, engine):
        """Create engine-specific configuration files"""
        source_path = project_path / "source"
        source_path.mkdir(exist_ok=True, parents=True)
        
        if engine == "Godot":
            # Create project.godot file
            project_godot = source_path / "project.godot"
            project_content = f"""[application]

config/name="{project_path.name}"
config/features=PackedStringArray("4.2", "Forward Plus")
config/icon="res://icon.svg"

[rendering]

renderer/rendering_method="forward_plus"
"""
            with open(project_godot, 'w') as f:
                f.write(project_content)
                
        elif engine == "Unity":
            # Create basic Unity project structure
            project_settings = source_path / "ProjectSettings" / "ProjectSettings.asset"
            project_settings.parent.mkdir(exist_ok=True, parents=True)
            
            packages_manifest = source_path / "Packages" / "manifest.json"
            packages_manifest.parent.mkdir(exist_ok=True, parents=True)
            
            manifest_content = """{
  "dependencies": {
    "com.unity.collab-proxy": "2.0.5",
    "com.unity.feature.development": "1.0.1",
    "com.unity.ide.rider": "3.0.24",
    "com.unity.ide.visualstudio": "2.0.18",
    "com.unity.ide.vscode": "1.2.5",
    "com.unity.inputsystem": "1.7.0",
    "com.unity.test-framework": "1.1.33",
    "com.unity.textmeshpro": "3.0.6",
    "com.unity.timeline": "1.7.5",
    "com.unity.ugui": "1.0.0",
    "com.unity.visualscripting": "1.9.0",
    "com.unity.modules.ai": "1.0.0",
    "com.unity.modules.androidjni": "1.0.0",
    "com.unity.modules.animation": "1.0.0",
    "com.unity.modules.assetbundle": "1.0.0",
    "com.unity.modules.audio": "1.0.0",
    "com.unity.modules.cloth": "1.0.0",
    "com.unity.modules.director": "1.0.0",
    "com.unity.modules.imageconversion": "1.0.0",
    "com.unity.modules.imgui": "1.0.0",
    "com.unity.modules.jsonserialize": "1.0.0",
    "com.unity.modules.particlesystem": "1.0.0",
    "com.unity.modules.physics": "1.0.0",
    "com.unity.modules.physics2d": "1.0.0",
    "com.unity.modules.screencapture": "1.0.0",
    "com.unity.modules.terrain": "1.0.0",
    "com.unity.modules.terrainphysics": "1.0.0",
    "com.unity.modules.tilemap": "1.0.0",
    "com.unity.modules.ui": "1.0.0",
    "com.unity.modules.uielements": "1.0.0",
    "com.unity.modules.umbra": "1.0.0",
    "com.unity.modules.unityanalytics": "1.0.0",
    "com.unity.modules.unitywebrequest": "1.0.0",
    "com.unity.modules.unitywebrequestassetbundle": "1.0.0",
    "com.unity.modules.unitywebrequestaudio": "1.0.0",
    "com.unity.modules.unitywebrequesttexture": "1.0.0",
    "com.unity.modules.unitywebrequestwww": "1.0.0",
    "com.unity.modules.vehicles": "1.0.0",
    "com.unity.modules.video": "1.0.0",
    "com.unity.modules.vr": "1.0.0",
    "com.unity.modules.wind": "1.0.0",
    "com.unity.modules.xr": "1.0.0"
  }
}"""
            with open(packages_manifest, 'w') as f:
                f.write(manifest_content)
                
        elif engine == "Unreal":
            # Create .uproject file
            uproject_file = source_path / f"{project_path.name}.uproject"
            uproject_content = f"""{{
	"FileVersion": 3,
	"EngineAssociation": "5.3",
	"Category": "",
	"Description": "",
	"Modules": [
		{{
			"Name": "{project_path.name}",
			"Type": "Runtime",
			"LoadingPhase": "Default"
		}}
	],
	"Plugins": [
		{{
			"Name": "ModelingToolsEditorMode",
			"Enabled": true,
			"TargetAllowList": [
				"Editor"
			]
		}}
	]
}}"""
            with open(uproject_file, 'w') as f:
                f.write(uproject_content)
    
    def configure_agents(self, project_details):
        """Determine which agents to activate based on project needs"""
        agents = ["master_orchestrator", "producer_agent"]
        
        # Market Analyst and Data Scientist are always included for data-driven decisions
        agents.extend(["market_analyst", "data_scientist"])
        
        # Add agents based on mode
        if project_details['mode'] == 'design':
            agents.extend([
                "sr_game_designer",
                "mid_game_designer",
                "sr_game_artist"
            ])
        elif project_details['mode'] == 'prototype':
            agents.extend([
                "sr_game_designer",
                "mechanics_developer",
                "qa_agent"
            ])
        elif project_details['mode'] == 'development':
            agents.extend([
                "sr_game_designer",
                "mid_game_designer",
                "mechanics_developer",
                "game_feel_developer",
                "qa_agent",
                "sr_game_artist",
                "technical_artist",
                "ui_ux_agent"
            ])
        
        return agents
    
    def calculate_milestones(self, timeline, mode):
        """Generate milestone schedule based on timeline and mode"""
        milestones = []
        today = datetime.now()
        
        if mode == 'design':
            if timeline == 'Rapid':
                milestones = [
                    {
                        "name": "Concept Complete",
                        "target_date": (today + timedelta(days=2)).strftime("%Y-%m-%d"),
                        "deliverables": ["Core concept", "Design pillars", "Target audience analysis"],
                        "success_criteria": ["Concept validated", "Scope defined"]
                    },
                    {
                        "name": "Design Documentation",
                        "target_date": (today + timedelta(days=5)).strftime("%Y-%m-%d"),
                        "deliverables": ["Complete GDD", "Art style guide", "Technical assessment"],
                        "success_criteria": ["All systems documented", "Feasibility confirmed"]
                    }
                ]
            elif timeline == 'Short':
                weeks = 3
                milestones = [
                    {
                        "name": "Concept Phase",
                        "target_date": (today + timedelta(weeks=1)).strftime("%Y-%m-%d"),
                        "deliverables": ["Game concept", "Market research", "Competitive analysis"],
                        "success_criteria": ["Unique value proposition", "Target audience defined"]
                    },
                    {
                        "name": "Systems Design",
                        "target_date": (today + timedelta(weeks=2)).strftime("%Y-%m-%d"),
                        "deliverables": ["Core systems", "Gameplay mechanics", "Progression design"],
                        "success_criteria": ["All systems mapped", "Dependencies identified"]
                    },
                    {
                        "name": "Complete Documentation",
                        "target_date": (today + timedelta(weeks=3)).strftime("%Y-%m-%d"),
                        "deliverables": ["Full GDD", "Art bible", "Technical specifications"],
                        "success_criteria": ["Ready for development", "All questions answered"]
                    }
                ]
        
        elif mode == 'development':
            if timeline == 'Short':
                milestones = [
                    {
                        "name": "Prototype",
                        "target_date": (today + timedelta(weeks=1)).strftime("%Y-%m-%d"),
                        "deliverables": ["Core mechanic", "Basic controls", "Placeholder art"],
                        "success_criteria": ["Playable prototype", "Core loop validated"]
                    },
                    {
                        "name": "Alpha",
                        "target_date": (today + timedelta(weeks=2)).strftime("%Y-%m-%d"),
                        "deliverables": ["All features", "Programmer art", "Basic UI"],
                        "success_criteria": ["Feature complete", "Internally playable"]
                    },
                    {
                        "name": "Beta",
                        "target_date": (today + timedelta(weeks=3)).strftime("%Y-%m-%d"),
                        "deliverables": ["Polished gameplay", "Final art", "Sound integrated"],
                        "success_criteria": ["No critical bugs", "Performance targets met"]
                    },
                    {
                        "name": "Release",
                        "target_date": (today + timedelta(weeks=4)).strftime("%Y-%m-%d"),
                        "deliverables": ["Final build", "Marketing materials", "Distribution ready"],
                        "success_criteria": ["Ship ready", "All platforms tested"]
                    }
                ]
            elif timeline == 'Medium':
                months = 2
                # Add more detailed milestones for medium timeline
                pass
        
        return milestones
    
    def initialize_project(self):
        """Main initialization flow"""
        print("\n" + "="*60)
        print("GAME STUDIO PROJECT INITIALIZER")
        print("="*60 + "\n")
        
        # Gather project information
        project_details = {}
        
        project_details['name'] = input("1. PROJECT NAME: ").strip()
        project_details['concept'] = input("2. GAME CONCEPT (one sentence): ").strip()
        
        print("\n3. TARGET PLATFORM:")
        print("   1) PC (Windows/Mac/Linux)")
        print("   2) Mobile (iOS/Android)")
        print("   3) Console")
        print("   4) Web Browser")
        print("   5) VR/AR")
        platform_choice = input("   Select (1-5): ").strip()
        platforms = ["PC", "Mobile", "Console", "Web", "VR/AR"]
        project_details['platform'] = platforms[int(platform_choice)-1] if platform_choice.isdigit() else "PC"
        
        print("\n4. TARGET AUDIENCE:")
        print("   1) Casual (All ages)")
        print("   2) Core (Regular gamers)")
        print("   3) Hardcore (Experienced)")
        print("   4) Kids (Age 3-12)")
        audience_choice = input("   Select (1-4): ").strip()
        audiences = ["Casual", "Core", "Hardcore", "Kids"]
        project_details['audience'] = audiences[int(audience_choice)-1] if audience_choice.isdigit() else "Core"
        
        print("\n5. DEVELOPMENT MODE:")
        print("   1) Design Only")
        print("   2) Full Development")
        print("   3) Prototype")
        mode_choice = input("   Select (1-3): ").strip()
        modes = ["design", "development", "prototype"]
        project_details['mode'] = modes[int(mode_choice)-1] if mode_choice.isdigit() else "design"
        
        print("\n6. TIMELINE:")
        print("   1) Rapid (< 1 week)")
        print("   2) Short (1-4 weeks)")
        print("   3) Medium (1-3 months)")
        print("   4) Long (3+ months)")
        timeline_choice = input("   Select (1-4): ").strip()
        timelines = ["Rapid", "Short", "Medium", "Long"]
        project_details['timeline'] = timelines[int(timeline_choice)-1] if timeline_choice.isdigit() else "Short"
        
        print("\n7. ENGINE:")
        print("   1) Godot")
        print("   2) Unity")
        print("   3) Unreal Engine")
        print("   4) No preference")
        engine_choice = input("   Select (1-4): ").strip()
        engines = ["Godot", "Unity", "Unreal", "TBD"]
        project_details['engine'] = engines[int(engine_choice)-1] if engine_choice.isdigit() else "Godot"
        
        print("\n8. GENRE:")
        print("   1) Action")
        print("   2) Strategy")
        print("   3) Puzzle")
        print("   4) RPG")
        print("   5) Simulation")
        print("   6) Adventure")
        print("   7) Casual/Arcade")
        genre_choice = input("   Select (1-7): ").strip()
        genres = ["Action", "Strategy", "Puzzle", "RPG", "Simulation", "Adventure", "Casual"]
        project_details['genre'] = genres[int(genre_choice)-1] if genre_choice.isdigit() else "Action"
        
        print("\n9. COMPETITOR GAMES:")
        project_details['competitors'] = input("   Name 1-3 games similar to your idea: ").strip()
        
        print("\n10. UNIQUE SELLING POINT:")
        project_details['usp'] = input("    What makes your game special? (one sentence): ").strip()
        
        # Create project structure
        print(f"\nCreating project structure for '{project_details['name']}'...")
        project_path = self.create_project_structure(project_details['name'], project_details['engine'])
        
        # Configure agents
        active_agents = self.configure_agents(project_details)
        
        # Generate milestones
        milestones = self.calculate_milestones(project_details['timeline'], project_details['mode'])
        
        # Build configuration
        config = {
            "project": {
                "name": project_details['name'],
                "concept": project_details['concept'],
                "genre": project_details['genre'],
                "platform": project_details['platform'],
                "audience": project_details['audience'],
                "timeline": project_details['timeline'],
                "engine": project_details['engine'],
                "mode": project_details['mode'],
                "competitors": project_details.get('competitors', ''),
                "unique_selling_point": project_details.get('usp', ''),
                "version": "1.0.0",
                "created": datetime.now().isoformat(),
                "phase": "Market Analysis",
                "status": "active"
            },
            "team": {
                "active_agents": active_agents,
                "lead_agent": "producer_agent",
                "orchestrator": "master_orchestrator"
            },
            "milestones": milestones,
            "metrics": {
                "velocity_target": "10 tasks/week",
                "bug_threshold": "5 critical, 20 minor",
                "performance_target": "60 FPS, < 3s load"
            },
            "risks": [
                {
                    "risk": "Scope creep",
                    "probability": "Medium",
                    "impact": "High",
                    "mitigation": "Strict feature freeze after design phase"
                }
            ]
        }
        
        # Create initial files
        print("Creating initial documentation...")
        self.create_initial_files(project_path, config)
        
        # Create customized agents for this project
        print("Creating project-specific agents...")
        agent_customizer = AgentCustomizer()
        agent_customizer.customize_agents_for_project(project_path, config)
        
        # Display summary
        print("\n" + "="*60)
        print("PROJECT INITIALIZED SUCCESSFULLY!")
        print("="*60)
        print(f"\nProject: {project_details['name']}")
        print(f"Location: {project_path.absolute()}")
        print(f"Mode: {project_details['mode'].upper()}")
        print(f"Active Agents: {len(active_agents)}")
        print(f"  - {', '.join(active_agents)}")
        print(f"\nMilestones: {len(milestones)}")
        for milestone in milestones:
            print(f"  - {milestone['name']}: {milestone['target_date']}")
        
        print("\n" + "-"*60)
        print("NEXT STEPS:")
        print("-"*60)
        print("1. Navigate to your project:")
        print(f"   cd projects/{project_details['name'].lower().replace(' ', '-')}")
        print("2. Review project-config.json for accuracy")
        print("3. Start with Market Analysis:")
        print("   claude 'Read agents/market_analyst.md and analyze the market for this project'")
        print("4. Then activate Project Orchestrator:")
        print("   claude 'Read agents/project_orchestrator.md and begin development'")
        print("5. Use project-specific agents (in agents/ folder) - they're customized for your engine!")
        print("\n💡 Your agents are customized for:")
        print(f"   - Engine: {project_details['engine']}")
        print(f"   - Platform: {project_details['platform']}")
        print(f"   - Genre: {project_details['genre']}")
        print("\nProject is ready for engine-optimized, market-driven development!")
        
        return project_path, config


if __name__ == "__main__":
    initializer = ProjectInitializer()
    initializer.initialize_project()