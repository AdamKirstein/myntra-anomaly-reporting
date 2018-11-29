from jinja2 import FileSystemLoader, Environment

# Content to be published
content = "Starting small just to make sure that this will work!"

# Configure Jinja and ready the template
env = Environment(
    loader=FileSystemLoader(searchpath="template")
)
template = env.get_template("report.html")


def main():
    """
    Entry point for the script.
    Render a template and write it to file.
    :return:
    """
    with open("output/report.html", "w") as f:
        f.write(template.render(content=content))


if __name__ == "__main__":
    main()