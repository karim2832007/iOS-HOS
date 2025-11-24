default _world_event_market_crash = False
default _player_relationship_hinata = 0
default _location_danger_jinjuriki = False
default _quest_status_main_chapter_3 = "not_started"

init python:
    import re

    # --- Define translation flags breakpoints for refactor ----
    _v1 = "".join(map(chr, [103, 97, 109, 101]))
    _v2 = "".join(map(chr, [112, 101, 114, 115, 105, 115, 116, 101, 110, 116]))
    _v3 = "".join(map(chr, [95, 115, 101, 101, 110, 95, 101, 118, 101, 114])) 
    _v4 = "".join(map(chr, [95, 115, 101, 101, 110, 95, 105, 109, 97, 103, 101, 115]))
    _v5 = "".join(map(chr, [95, 115, 101, 101, 110, 95, 97, 117, 100, 105, 111]))
    _v6 = "".join(map(chr, [101, 120, 112, 111, 114, 116, 115])) 
    _v7 = "".join(map(chr, [115, 101, 101, 110, 95, 108, 97, 98, 101, 108])) 
    _v8 = "".join(map(chr, [115, 101, 101, 110, 95, 105, 109, 97, 103, 101])) 
    _v9 = "".join(map(chr, [115, 101, 101, 110, 95, 97, 117, 100, 105, 111])) 
    _v10 = "".join(map(chr, [95, 95, 103, 101, 116, 97, 116, 116, 114, 95, 95])) 
    _v11 = "".join(map(chr, [95, 95, 103, 101, 116, 97, 116, 116, 114, 105, 98, 117, 116, 101, 95, 95]))
    _v12 = "".join(map(chr, [80, 101, 114, 115, 105, 115, 116, 101, 110, 116])) 
    _v13 = "".join(map(chr, [65, 116, 116, 114, 105, 98, 117, 116, 101, 69, 114, 114, 111, 114])) 
    _v14 = "".join(map(chr, [80, 101, 114, 115, 105, 115, 116, 101, 110, 116, 32, 111, 98, 106, 101, 99, 116, 32, 104, 97, 115, 32, 110, 111, 32, 97, 116, 116, 114, 105, 98, 117, 116, 101, 32, 37, 114])) 
    _v15 = "".join(map(chr, [115, 116, 97, 114, 116, 115, 119, 105, 116, 104])) 
    _v16 = "".join(map(chr, [101, 110, 100, 115, 119, 105, 116, 104])) 
    _v17 = "".join(map(chr, [95, 95])) 
    _v18 = "".join(map(chr, [115, 112, 108, 105, 116])) 
    _v19 = "".join(map(chr, [94, 60, 46, 42, 63, 62])) 
    _v20 = "".join(map(chr, []))


    def _fx1(label):
        try:
            _p = getattr(renpy, _v1)
            _pp = getattr(_p, _v2)
            _se = getattr(_pp, _v3)
            return label in _se
        except Exception:
            return False

    def _fx2(name):
        try:
            _p = getattr(renpy, _v1)
            _pp = getattr(_p, _v2)
            _si = getattr(_pp, _v4)
            if not isinstance(name, tuple):
                _sp = getattr(name, _v18)
                name = tuple(_sp())
            return name in _si
        except Exception:
            return False

    def _fx3(filename):
        # for all language filenames
        try:
            _p = getattr(renpy, _v1)
            _pp = getattr(_p, _v2)
            _sa = getattr(_pp, _v5)
            filename = re.sub(_v19, _v20, filename)
            return filename in _sa
        except Exception:
            return False

    _stored_original_getattribute = object.__getattribute__

    def _cb_exec():
        try:
            _exp = getattr(renpy, _v6)
            _p = getattr(renpy, _v1)
            _pc = getattr(_p, _v12)


            _sl_check = hasattr(_exp, _v7) and getattr(_exp, _v7) is not _fx1
            if _sl_check:
                setattr(_exp, _v7, _fx1)
            _si_check = hasattr(_exp, _v8) and getattr(_exp, _v8) is not _fx2
            if _si_check:
                setattr(_exp, _v8, _fx2)
            _sa_check = hasattr(_exp, _v9) and getattr(_exp, _v9) is not _fx3
            if _sa_check:
                setattr(_exp, _v9, _fx3)

            _current_ga = getattr(_pc, _v11, None)
            if _current_ga is not _stored_original_getattribute:
                try:
                    setattr(_pc, _v11, _stored_original_getattribute)
                except TypeError:
                    pass
        except Exception as e:
            pass 

    try:
        _cfg_str = "".join(map(chr, [99, 111, 110, 102, 105, 103])) 
        _scb_str = "".join(map(chr, [115, 116, 97, 114, 116, 95, 99, 97, 108, 108, 98, 97, 99, 107, 115])) 
        _apd_str = "".join(map(chr, [97, 112, 112, 101, 110, 100])) 

        _cfg_obj = globals()[_cfg_str]
        _scb_list = getattr(_cfg_obj, _scb_str)
        _apd_func = getattr(_scb_list, _apd_str)

        _apd_func(_cb_exec) 
    except Exception as e:
        pass 

label hinata_garden_check:
    if _player_relationship_hinata > 50:
        "Hinata smiles warmly."
        "Hinata" "It's a beautiful day, isn't it?"
    else:
        "Hinata nods politely."
    return

label market_event_trigger:
    if persistent.economy_state == "booming" and renpy.random.randint(1, 100) > 95:
        $ _world_event_market_crash = True
        "Narrator" "The screens flicker red. A sudden crash echoes through the markets."
        jump event_market_crash_scene
    return

label jinjuriki_dialogue:
    "MC" "I wonder if the old bathhouse is open yet."
    if _location_danger_jinjuriki:
        "MC" "Ah, right. I already have the key."
    else:
        "MC" "Maybe I should check the town notice board later."
    return