## Here are all the functions and classes to run the system. 
## Please, if you don't know how works Python, don't touch anything !

init python:
    import collections

## This class lets the dev create some events for his game. By default, all the events have the 
## pending state and are hidden.
    class Quest:
        def __init__(self, id, title, category,  state= "pending", wip=False, questlevel=1):
            self.id = id
            self.title = title
            self.category = category
            self.state = state
            self.wip = wip
            self.questlevel = questlevel

        def __repr__(self):
            return "<Lvl {} - {}>".format(self.questlevel, self.title)





## This class allows the developer to perform various operations on the events
    class Manager:


        # ... (existing code remains the same)

        def change_quest_title(self, id, new_title):
            """
            Change the title of a quest based on its ID.
            
            :param id: The ID of the quest to be updated
            :param new_title: The new title for the quest
            :return: True if the quest was found and updated, False otherwise
            """
            quest = self._searchID(id)
            if quest:
                quest.title = new_title
                print(f"Quest '{id}' title updated to: {new_title}")
                return True
            
            print(f"Quest with ID '{id}' not found.")
            return False

    # ... (rest of the existing code)

        def __init__(self):
            self.quests_dict = collections.OrderedDict() ## The place where are loaded the events 
            self.states = ["pending", "unlocked", "in progress", "WIP", "completed", "done", "failed", "canceled"]


#_______Loading and deleting chapter into the manager_______________

        ## Load the chapter into the manager memory
        def load(self, chapter):
            if type(chapter) is not tuple:
                print("Error: must be a tuple")
                renpy.quit()
            self.quests_dict.clear()
            for quest in chapter:
                if quest.category not in self.quests_dict:
                    self.quests_dict[quest.category] = collections.OrderedDict([(quest.id,quest)])
                else:
                    self.quests_dict[quest.category][quest.id] = quest
            self._reload_screen("diary")
            renpy.block_rollback()
            print(self.quests_dict)

        ## Synchronizes the manager with a master list of quest definitions.
        ## This is the master function for loading and patching quests.
        def synchronize(self, source):
            """
            Synchronizes the manager from a source.
            The source can be:
            1. A tuple of Quest objects (e.g., boruto1).
            2. A string base name (e.g., "hinata") to dynamically find all
            quest definitions like "hinata1", "hinata2", etc.
            """
            print(f"--- Manager.synchronize called with source: {source} ---")
            
            chapter_definitions = ()

            # --- PART 1: COLLECT QUEST DEFINITIONS ---
            if isinstance(source, str):
                # If the source is a string, dynamically find all matching definitions.
                base_name = source
                print(f"  [Sync] Source is a string. Collecting all definitions with base name: '{base_name}'...")
                for var_name in dir(renpy.store):
                    if var_name.startswith(base_name):
                        suffix = var_name[len(base_name):]
                        if suffix.isdigit():
                            print(f"    -> Found quest definition variable: {var_name}")
                            quest_tuple = getattr(renpy.store, var_name)
                            if isinstance(quest_tuple, tuple):
                                chapter_definitions += quest_tuple
            
            elif isinstance(source, tuple):
                # If the source is already a tuple, just use it directly.
                print("  [Sync] Source is a tuple. Using it directly.")
                chapter_definitions = source
            
            else:
                print(f"  [Sync] ERROR: Invalid source type for synchronize: {type(source)}. Aborting.")
                return

            # --- PART 2: ADD MISSING QUESTS ---
            # ... (The rest of the function logic is identical to before) ...
            definitions_map = {q.id: q for q in chapter_definitions}

            for quest_def in chapter_definitions:
                if not self._searchID(quest_def.id):
                    print(f"\n[Sync Add] New quest '{quest_def.id}' found in definitions. Adding to manager.")
                    self.add(quest_def)

            # --- PART 3: UPDATE ATTRIBUTES OF ALL QUESTS ---
            print("\n--- Beginning attribute sync for all quests in manager... ---")
            for category in self.quests_dict.values():
                for loaded_quest in category.values():
                    # ... (This entire loop for syncing title, wip, questlevel is unchanged) ...
                    print(f"\n[DIAGNOSTIC] Processing loaded quest: '{loaded_quest.id}'")
                    if loaded_quest.id in definitions_map:
                        fresh_definition = definitions_map[loaded_quest.id]
                        if loaded_quest.title != fresh_definition.title:
                            print(f"  - Syncing Title: Saved='{loaded_quest.title}' -> Definition='{fresh_definition.title}'")
                            loaded_quest.title = fresh_definition.title
                        else:
                            print(f"  - Title is already in sync.")

                        # Get the WIP status from the fresh definition file (the "source of truth"). Defaults to False.
                        defined_wip = getattr(fresh_definition, 'wip', False)
                        # Get the WIP status from the loaded save data. Defaults to False for old saves without the flag.
                        saved_wip = getattr(loaded_quest, 'wip', False)
                        # Now, perform a clean and unambiguous comparison.
                        if saved_wip != defined_wip:
                            if not hasattr(loaded_quest, 'wip'):
                                print(f"  - Patching missing .wip attribute. Setting to Definition: {defined_wip}")
                            else:
                                print(f"  - Syncing WIP: Saved={saved_wip} -> Definition={defined_wip}")
                            # In either case, update the loaded quest to match the definition.
                            loaded_quest.wip = defined_wip
                        else:
                            print(f"  - WIP status is already in sync (Value: {saved_wip}).")
                        defined_level = getattr(fresh_definition, 'questlevel', 1)
                        saved_level = getattr(loaded_quest, 'questlevel', 1)
                        if saved_level != defined_level:
                            print(f"  - Syncing Quest Level: Saved={saved_level} -> Definition={defined_level}")
                            loaded_quest.questlevel = defined_level
                        else:
                            print(f"  - Quest Level is already in sync (Value: {saved_level}).")
                    else:
                        print(f"  - WARNING: Quest '{loaded_quest.id}' exists in save but has no definition in the script. Cannot synchronize.")

        ## Delete the chapter from the manager memory
        def free(self):
            self.quests_dict.clear()
            renpy.block_rollback()



#____________Search functions to find some events______________

        def _search(self, id, category = ""):
            if category == "":
                return self._searchID(id)
            return self.quests_dict[category][id]


        def _searchID(self, id):
            for k in self.quests_dict.keys():
                if id in self.quests_dict[k]:
                    return self.quests_dict[k][id]

        def _find_master_quest_for_category(self, category_name):
            """
            Finds the quest object that serves as the master quest for a given category.
            This works by finding the quest whose 'title' matches the 'category_name'.
            Returns the Quest object or None if not found.
            """
            # This is a good candidate for caching if performance ever becomes an issue,
            # but a direct search is fine for most cases.
            for category in self.quests_dict.values():
                for quest in category.values():
                    if quest.title == category_name:
                        return quest
            return None


#____________Functions to do some tests_____________________

        ## Return True if the quest is NOT a WIP, False otherwise.
        ## Designed to be safe with old saves.
        def is_implemented(self, id):
            quest_obj = self._searchID(id)
            if not quest_obj:
                return False # A quest that doesn't exist is not implemented.

            # Check if the object has the 'wip' attribute.
            # This is the key for backwards compatibility.
            if hasattr(quest_obj, 'wip'):
                # The attribute exists, so we return its value (inversely).
                return not quest_obj.wip
            else:
                # The attribute DOES NOT exist. This is an old save.
                # Per your design, its lack implies it IS implemented.
                return True

        ## Return True if the category exists in the chapter
        def exists(self, id, category = ""):
            if self._search(id, category):
                return True
            return False


        ## Return the category
        def is_in(self, id):
            for k in self.quests_dict.keys():
                if id in self.quests_dict[k]:
                    return k


        ## Return True if the ID has the right state
        def is_state(self, id, state, category = ""):
            if self._search(id, category).state == state:
                return True
            return False

        ## Return True if all the events of a category are done
        def is_category_over(self, category):
            for v in self.quests_dict[category].values():
                if v.state != "done":
                    return False
            return True

        ## Return True if all the events from all the categories are done
        def is_chapter_over(self):
            for k in self.quests_dict.keys():
                if not self.is_category_over(k):
                    return False
            return True


#_____________Some functions to change the state of quests__________________

        ## Check if the event has the right state, otherwise it is updated
        def check(self, id, state, category = ""):
            if state not in self.states:
                print("Error: this state doesn't exist ! Please check the documentation.")
                return
            if category == "" and state != "canceled":
                self._checkID(id, state)
                return
            if state == "canceled":
                self._remove_quest(id)
                return
            self._search(id, category).state = state
            print("{} {}".format(id ,self._search(id, category).state))
            

        ## Private function to find an event by his ID
        def _checkID(self, id, state):
            self._searchID(id).state = state



        def update(self, id="", state="", unchanged = [], category=""):
            temp = False
            if isinstance(id, tuple):
                id1, id2 = id
            else:
                id1, id2 = id, id
                temp = True
            if isinstance(state, tuple):
                state1, state2 = state
            else:
                state1, state2 = state, state

            if category == "" and id != "":
                category = self._searchID(id2).category  

            if id == "" and category != "":
                self._update_all_quests(state, unchanged, category)
                return

            for k,v, in self.quests_dict[category].items():
                if k == id1:
                    temp = True 
                if k == id2:
                    v.state = state2
                    return
                if temp == True:
                    if v.state not in unchanged:
                        v.state = state1


        def _update_all_quests(self, state="", unchanged = [], category=""):
            for k,v, in self.quests_dict[category].items():
                if v.state not in unchanged:
                    v.state = state


#_____________Add or remove categories from the chapter___________

        ## Add a new category into the chapter during the game 
        ## The added categories will not be stored when the chapter is freed
        def add(self, quests):
            if isinstance(quests, (list, tuple)): # Change this line to accept tuples as well
                self._add_multi(quests)
                return
            if self.exists(quests.id):
                print("Error: already in quests_dict")
                return
            if quests.category not in self.quests_dict:
                self.quests_dict[quests.category] = collections.OrderedDict([(quests.id,quests)])
            else:
                self.quests_dict[quests.category][quests.id] = quests


        def _add_multi(self, quest_list):
            for quest in quest_list:
                self.add(quest)

        ## Remove a category from the category
        def remove(self, category):
            if category not in self.quests_dict:
                return
            del self.quests_dict[category]
            self._reload_screen("diary")


        def _remove_quest(self, id, category = ""):
            if category == "":
                category = self.is_in(id)
            del self.quests_dict[category][id]
            if self.quests_dict[category] == {}:
                del self.quests_dict[category]



        ## If a category is deleted and the log is open, you have to reload the screen
        def _reload_screen(self, screen_name):
            if renpy.get_screen(screen_name):
                renpy.hide_screen(screen_name)
                renpy.show_screen(screen_name)
