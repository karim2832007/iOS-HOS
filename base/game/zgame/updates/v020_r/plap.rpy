# transform rhythmic_motion(intensity=20, speed=0.5, duration=5.0):
#     linear 0.0 yoffset 0
#     block:
#         linear speed yoffset intensity
#         linear speed yoffset -intensity
#         repeat int(duration / (speed * 2))

# # Advanced motion with multiple effects
# transform dynamic_motion(intensity=25, shake_power=5, duration=10.0):
#     # Initial setup
#     alpha 1.0 zoom 1.0 yoffset 0 xoffset 0
    
#     block:
#         # Main rhythmic movement
#         parallel:
#             linear 0.3 yoffset intensity
#             linear 0.3 yoffset -intensity/2
#             linear 0.3 yoffset intensity
#             linear 0.3 yoffset 0
#             repeat int(duration / 1.2)
        
#         # Subtle shake effect
#         parallel:
#             linear 0.1 xoffset shake_power
#             linear 0.1 xoffset -shake_power
#             linear 0.1 xoffset 0
#             repeat int(duration / 0.3)
        
#         # Zoom pulsing
#         parallel:
#             linear 0.6 zoom 1.05
#             linear 0.6 zoom 0.98
#             linear 0.6 zoom 1.02
#             linear 0.6 zoom 1.0
#             repeat int(duration / 2.4)

# # Motion with blur effect (requires blur shader)
# transform motion_with_blur(intensity=30, duration=8.0):
#     # Note: Blur requires additional shader setup
#     block:
#         parallel:
#             linear 0.4 yoffset intensity
#             linear 0.4 yoffset -intensity/3
#             repeat int(duration / 0.8)
        
#         parallel:
#             linear 0.2 blur 2.0
#             linear 0.2 blur 0.0
#             repeat int(duration / 0.4)

# # Intense motion with screen effects
# transform intense_motion(power=40, duration=6.0):
#     alpha 1.0
#     block:
#         # Strong vertical motion
#         parallel:
#             ease 0.25 yoffset power
#             ease 0.25 yoffset -power/2
#             ease 0.25 yoffset power/1.5
#             ease 0.25 yoffset 0
#             repeat int(duration / 1.0)
        
#         # Horizontal sway
#         parallel:
#             linear 0.8 xoffset 10
#             linear 0.8 xoffset -10
#             linear 0.8 xoffset 5
#             linear 0.8 xoffset 0
#             repeat int(duration / 3.2)
        
#         # Rotation for extra dynamics
#         parallel:
#             linear 0.6 rotate 1
#             linear 0.6 rotate -1
#             linear 0.6 rotate 0
#             repeat int(duration / 1.8)

# # Customizable motion builder
# transform custom_motion(y_intensity=25, x_intensity=10, zoom_range=0.05, speed=0.3, duration=10.0, with_rotation=False):
#     block:
#         # Vertical motion
#         parallel:
#             linear speed yoffset y_intensity
#             linear speed yoffset -y_intensity/2
#             repeat int(duration / (speed * 2))
        
#         # Horizontal motion
#         parallel:
#             linear speed*2 xoffset x_intensity
#             linear speed*2 xoffset -x_intensity
#             repeat int(duration / (speed * 4))
        
#         # Zoom effects
#         parallel:
#             linear speed*3 zoom (1.0 + zoom_range)
#             linear speed*3 zoom (1.0 - zoom_range/2)
#             repeat int(duration / (speed * 6))
        
 

# # Screen shake for background/UI elements
# transform screen_shake(power=15, duration=3.0):
#     linear 0.0 xoffset 0 yoffset 0
#     block:
#         linear 0.05 xoffset power yoffset power/2
#         linear 0.05 xoffset -power yoffset -power/2
#         linear 0.05 xoffset power/2 yoffset power
#         linear 0.05 xoffset -power/2 yoffset -power
#         linear 0.05 xoffset 0 yoffset 0
#         repeat int(duration / 0.25)





# transform bouncy_plap_random:
#     xalign 0.5 yalign 0.5
#     alpha 0.0 zoom 0.5
    
#     # Bouncy entrance
#     parallel:
#         ease 0.15 alpha 1.0 zoom 1.3
#         ease 0.15 zoom 0.9
#         ease 0.1 zoom 1.1
#         ease 0.1 zoom 1.0
    
#     # Drift and fade
#     parallel:
#         linear 1.0 yoffset -60 xoffset 20
#     parallel:
#         linear 0.4 alpha 1.0
#         linear 0.6 alpha 0.0

# # Simple random positioning transforms
# transform plap_left:
#     anchor (0.5, 0.5)
#     pos (400, 500)
#     alpha 0.0 zoom 0.8
#     ease 0.1 alpha 1.0 zoom 1.2
#     ease 0.2 zoom 1.0
#     parallel:
#         linear 1.2 ypos 420
#     parallel:
#         linear 0.3 alpha 1.0
#         linear 0.9 alpha 0.0

# transform plap_center:
#     anchor (0.5, 0.5)
#     pos (640, 520)
#     alpha 0.0 zoom 0.8
#     ease 0.1 alpha 1.0 zoom 1.2
#     ease 0.2 zoom 1.0
#     parallel:
#         linear 1.2 ypos 440
#     parallel:
#         linear 0.3 alpha 1.0
#         linear 0.9 alpha 0.0

# transform plap_right:
#     anchor (0.5, 0.5)
#     pos (880, 510)
#     alpha 0.0 zoom 0.8
#     ease 0.1 alpha 1.0 zoom 1.2
#     ease 0.2 zoom 1.0
#     parallel:
#         linear 1.2 ypos 430
#     parallel:
#         linear 0.3 alpha 1.0
#         linear 0.9 alpha 0.0

# # Rapid-fire plap text function
# init python:
#     # Global variable to control continuous plaps
#     continuous_plaps_active = False
#     plap_counter = 0
    
#     def show_plap_burst(count=3, delay=0.3):
#         """Show multiple plap texts in quick succession"""
#         transforms = [plap_left, plap_center, plap_right]
#         for i in range(count):
#             chosen_transform = transforms[i % len(transforms)]
#             renpy.show("plap_text_{}".format(i), 
#                     what=Text("Plap", size=60, color="#ffffff", outlines=[(2, "#000000", 0, 0)]),
#                     at_list=[chosen_transform])
#             if i < count - 1:
#                 renpy.pause(delay, hard=True)
    
#     def show_random_plap():
#         """Show a single plap at a random position"""
#         import random
#         transforms = [plap_left, plap_center, plap_right]
#         chosen_transform = random.choice(transforms)
#         renpy.show("plap_text_random", 
#                 what=Text("Plap", size=60, color="#ffffff", outlines=[(2, "#000000", 0, 0)]),
#                 at_list=[chosen_transform])
    
#     def start_continuous_plaps(interval=1.0):
#         """Start showing continuous plaps until stopped"""
#         global continuous_plaps_active
#         continuous_plaps_active = True
#         renpy.call_in_new_context("continuous_plap_loop", interval)
    
#     def stop_continuous_plaps():
#         """Stop the continuous plaps"""
#         global continuous_plaps_active
#         continuous_plaps_active = False
    
#     def show_bouncy_plap():
#         """Show a single bouncy plap with random positioning"""
#         global plap_counter
#         plap_counter += 1
#         renpy.show("bouncy_plap_{}".format(plap_counter), 
#                 what=Text("Plap", size=60, color="#ffffff", outlines=[(2, "#000000", 0, 0)]),
#                 at_list=[bouncy_plap_random])

# # Label for continuous plap loop
# label continuous_plap_loop(interval=1.0):
#     while continuous_plaps_active:
#         $ show_bouncy_plap()
#         $ renpy.pause(interval, hard=True)
#     return

# # Style definitions for plap text
# style plap_text:
#     size 65
#     color "#ffffff"
#     outlines [(3, "#ff6b9d", 0, 0), (2, "#000000", 0, 0)]
#     font "DejaVuSans-Bold.ttf"  # Use a bold font if available

# style plap_text_small:
#     size 45
#     color "#ffaec9"
#     outlines [(2, "#ff1744", 0, 0), (1, "#000000", 0, 0)]