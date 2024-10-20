"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

#import asyncio
##import base64
#import datetime
#import os
#from dotenv import load_dotenv
#from hume.client import AsyncHumeClient
#from hume.empathic_voice.chat.socket_client import ChatConnectOptions, ChatWebsocketConnection
#from hume.empathic_voice.chat.types import SubscribeEvent
#from hume.empathic_voice.types import UserInput
#from hume.core.api_error import ApiError
#from hume import MicrophoneInterface, Stream

def ask_question(question: str):
    # This function sends the question to Hume's API and returns the voice response
    # You'll need to handle this with an API call to Hume
    # This is a placeholder implementation
    response = send_question_to_hume(question)
    return response

def send_question_to_hume(question: str):
    # Implement your call to Hume's API here
    # Send `question` and return a response
    pass

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
            rx.image(src="/ws.png", style={
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
            rx.link(
    rx.button(
    "Learn!", style={
        "position": "absolute",  # Allows you to set coordinates
        "top": "500px",          # Distance from the top of the container
        "left": "550px",         # Distance from the left of the container
        "zIndex": "10",          # Ensures it appears above other elements if necessary
        "width": "250px",        # Set the width of the button
        "height": "75px",        # Set the height of the button
        "padding": "15px",       # Adds padding inside the button to increase its size
        "fontSize": "65px",      # Increases the font size for better readability
    }),
    href="https://www.hume.ai",
    is_external=True
),
            #rx.button("Get Started", on_click=State.button_click, style={
                #"padding": "10px 20px",
                #"backgroundColor": "blue",
                #"color": "white",
                #"borderRadius": "5px",
                #"margin": "10px"
            #}),
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
