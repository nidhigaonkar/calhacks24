"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.image(src="/M.png", style={
                "position": "absolute",  # Allows you to set exact coordinates
                "top": "550px",          # Distance from the top of the container
                "left": "275px",          # Distance from the left of the container
                "width": "170px",        # Image width
                "height": "170px"        # Image height
            }),
            rx.image(src="/wai.png", style={
                "position": "absolute",  # Allows you to set exact coordinates
                "top": "550px",          # Distance from the top of the container
                "right": "275px",          # Distance from the left of the container
                "width": "170px",        # Image width
                "height": "170px"        # Image height
            }),
            rx.heading(
    "Webly: A one-stop platform where you can improve your internet literacy and navigate the web with ease.",
    size="9",
    position="relative",
    bottom="100px",  # Moves the heading down by 100px
    style={"textAlign": "center", "width": "100%"}  # Centers the heading
),
            #rx.text(
                #"Get started by editing ",
                #rx.code(f"{config.app_name}/{config.app_name}.py"),
                #size="5",
            #),
            #rx.link(
                #rx.button("Check out our docs!"),
                #href="https://reflex.dev/docs/getting-started/introduction/",
                #is_external=True,
            #),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="teal"
    )
)
app.add_page(index)
