#!/usr/bin/env python3
"""
* Talk to User is a simple tool that accepts user input and returns it as
* output. It serves as a basic example of a tool and can be extended for
* features such as presidio or CRITIC to further refine language model outputs.
"""

# Third-party modules
from dotenv import load_dotenv
# User-defined modules
from core.common import get_logger, get_mock_speaker
from core.classes import ActionStep, AbstractTool

load_dotenv()
logging = get_logger(name="tools.core.talk_to_user")


class TalkToUser(AbstractTool):
    """A service to manage and interact with Home Assistant."""

    def __init__(self):
        super().__init__(
            name="Talk to User",
            description="Directly talk to the user."
        )

    def set_state(self, action_step: ActionStep) -> "MockSpeaker":
        """
        An abstract method that subclasses should implement,
        performing the desired action.

        Returns:
            str: A message indicating the result of the action.
        """
        MockSpeaker = get_mock_speaker()
        return MockSpeaker(content=action_step.action_argument)

    def get_state(self, *args, **kwargs):
        raise NotImplementedError("This method is not supported by TalkToUser.")
