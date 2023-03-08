from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Any

import pygame

from ._types import EventDict

class State(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def update(self, events: EventDict, data: Dict[Any, Any]):
        pass
    
    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass
    
class State1(State):
    font = pygame.Font("assets/fonts/Cinzel.ttf")
    text = font.render("State1", True, "red")
    def __init__(self):
        super().__init__()
        self.pos = pygame.Vector2(0, 0)
    
    def update(self, events: EventDict, data: Dict[Any, Any]):
        self.pos += pygame.Vector2(1, 1) * 30 * data['dt']

    def draw(self, screen: pygame.Surface):
        screen.fill("black")
        screen.blit(State1.text, self.pos)
        
class State2(State):
    font = pygame.Font("assets/fonts/Cinzel.ttf")
    text = font.render("State2", True, "blue")
    def __init__(self):
        super().__init__()
        self.pos = pygame.Vector2(0, 0)
    
    def update(self, events: EventDict, data: Dict[Any, Any]):
        self.pos += pygame.Vector2(1, 1) * 30 * data['dt']

    def draw(self, screen: pygame.Surface):
        screen.fill("black")
        screen.blit(State2.text, self.pos)