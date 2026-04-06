"""Briefcase desktop app entry point."""


def main():
    """Launch the KohakuTerrarium desktop app."""
    from kohakuterrarium.serving.web import run_desktop_app

    run_desktop_app()
