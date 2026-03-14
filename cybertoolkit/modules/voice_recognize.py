import speech_recognition as sr
from rich.console import Console

console = Console()

def tool_info():
    return {
        "id": "voice",
        "name": "Voice Recognition",
        "run": run
    }

def run(args):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        console.print("[cyan]Listening... Speak now![/cyan]")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            console.print(f"[green]Recognized: {text}[/green]")
            # Optionally, process the text as a command
            if text.lower().strip() == "exit":
                console.print("[yellow]Voice command: exit[/yellow]")
            elif text.lower().startswith("run"):
                cmd = text.lower().replace("run", "").strip()
                console.print(f"[cyan]Voice command: {cmd}[/cyan]")
                # Could dispatch to registry, but for now just print
        except sr.WaitTimeoutError:
            console.print("[red]No speech detected[/red]")
        except sr.UnknownValueError:
            console.print("[red]Could not understand audio[/red]")
        except sr.RequestError as e:
            console.print(f"[red]Error: {e}[/red]")