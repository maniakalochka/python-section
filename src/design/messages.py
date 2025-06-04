import enum
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass


class MessageType(enum.Enum):
    TELEGRAM = enum.auto()
    MATTERMOST = enum.auto()
    SLACK = enum.auto()


@dataclass
class JsonMessage:
    message_type: MessageType
    payload: str


@dataclass
class ParsedMessage:
    """There is no need to describe anything here."""


class BaseParser(ABC):
    @abstractmethod
    def parse(self, message: JsonMessage) -> ParsedMessage:
        raise NotImplementedError("Subclasses must implement this method.")


class TelegramParser(BaseParser):
    def parse(self, message: JsonMessage) -> ParsedMessage:
        data = json.loads(message.payload)
        return (
            ParsedMessage()
        )  # Внутри ParsedMessage должна быть логика, но для краткости оставим пустым


class MattermostParser(BaseParser):
    def parse(self, message: JsonMessage) -> ParsedMessage:
        data = json.loads(message.payload)
        return ParsedMessage()  # Аналогично, как и в TelegramParser логику я не писал


class SlackParser(BaseParser):
    def parse(self, message: JsonMessage) -> ParsedMessage:
        data = json.loads(message.payload)
        return ParsedMessage()  # Аналогично, как и в TelegramParser логику я не писал


class ParserFactory:
    _parsers = {
        MessageType.TELEGRAM: TelegramParser(),
        MessageType.MATTERMOST: MattermostParser(),
        MessageType.SLACK: SlackParser(),
    }

    @classmethod
    def get_parser(cls, message_type: MessageType) -> BaseParser:
        if message_type not in cls._parsers:
            raise ValueError(f"No parser found for message type: {message_type}")
        return cls._parsers[message_type]
