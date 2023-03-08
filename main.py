from typing import Any, Dict

import pygame

pygame.init()

from src.state import State1, State2
from src._types import EventDict

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

state1 = State1()
state2 = State2()
current_state = state1

running = True
while running:
    events: EventDict = {}
    data: Dict[Any, Any] = {}
    data['dt'] = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type in events:
            events[event.type].append(event)
        else:
            events[event.type] = [event]
            
    if pygame.QUIT in events:
        running = False
    
    if pygame.KEYDOWN in events:
        if any(e.key == pygame.K_ESCAPE for e in events[pygame.KEYDOWN]):
            if current_state == state1:
                current_state = state2
            else:
                current_state = state1
        
    current_state.update(events, data)
    current_state.draw(screen)
    pygame.display.flip()