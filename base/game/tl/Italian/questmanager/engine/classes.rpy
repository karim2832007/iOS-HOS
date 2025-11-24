# Ren'Py Italian translation for classes
# Source Path: game/questmanager/engine/classes.rpy
# Generated: 2025-09-13T17:42:29.677625

translate Italian strings:

    # game/questmanager/engine/classes.rpy:6 "Error: this state doesn't exist ! Please check the documentation."
    old "Error: this state doesn't exist ! Please check the documentation."
    new "Errore: questo stato non esiste! Si prega di controllare la documentazione."

    # game/questmanager/engine/classes.rpy:6 "- Quest Level is already in sync (Value: {saved_level})."
    old "- Quest Level is already in sync (Value: {saved_level})."
    new "- Il livello della missione è già sincronizzato (Valore: {saved_level})."

    # game/questmanager/engine/classes.rpy:9 "canceled"
    old "canceled"
    new "canceled"

    # game/questmanager/engine/classes.rpy:12 "and category != "
    old "and category != "
    new "and category !="

    # game/questmanager/engine/classes.rpy:12 "- Syncing Title: Saved='{loaded_quest.title}' -> Definition='{fresh_definition.title}'"
    old "- Syncing Title: Saved='{loaded_quest.title}' -> Definition='{fresh_definition.title}'"
    new "- Sincronizzazione del titolo: Salvato='{loaded_quest.title}' -> Definizione='{fresh_definition.title}'"

    # game/questmanager/engine/classes.rpy:15 "diary"
    old "diary"
    new "diary"

    # game/questmanager/engine/classes.rpy:18 "pending"
    old "pending"
    new "pending"

    # game/questmanager/engine/classes.rpy:21 "unlocked"
    old "unlocked"
    new "unlocked"

    # game/questmanager/engine/classes.rpy:21 "-> Found quest definition variable: {var_name}"
    old "-> Found quest definition variable: {var_name}"
    new "-> Trovata variabile di definizione della missione: {var_name}"

    # game/questmanager/engine/classes.rpy:24 ", unchanged = [], category="
    old ", unchanged = [], category="
    new ", unchanged = [], category="

    # game/questmanager/engine/classes.rpy:24 "- Syncing WIP: Saved={saved_wip} -> Definition={defined_wip}"
    old "- Syncing WIP: Saved={saved_wip} -> Definition={defined_wip}"
    new "- Sincronizzazione WIP: Salvato={saved_wip} -> Definizione={defined_wip}"

    # game/questmanager/engine/classes.rpy:27 "and id != "
    old "and id != "
    new "e id !="

    # game/questmanager/engine/classes.rpy:27 "- WIP status is already in sync (Value: {saved_wip})."
    old "- WIP status is already in sync (Value: {saved_wip})."
    new "- Lo stato WIP è già sincronizzato (Valore: {saved_wip})."

    # game/questmanager/engine/classes.rpy:30 "[Sync] ERROR: Invalid source type for synchronize: {type(source)}. Aborting."
    old "[Sync] ERROR: Invalid source type for synchronize: {type(source)}. Aborting."
    new "[Sync] ERRORE: Tipo di sorgente non valido per la sincronizzazione: {type(source)}. Interruzione."

    # game/questmanager/engine/classes.rpy:30 "failed"
    old "failed"
    new "failed"

    # game/questmanager/engine/classes.rpy:33 "Quest with ID '{id}' not found."
    old "Quest with ID '{id}' not found."
    new "Missione con ID '{id}' non trovata."

    # game/questmanager/engine/classes.rpy:33 "\n[DIAGNOSTIC] Processing loaded quest: '{loaded_quest.id}'"
    old "\n[DIAGNOSTIC] Processing loaded quest: '{loaded_quest.id}'"
    new "\n[DIAGNOSTICA] Elaborazione della missione caricata: '{loaded_quest.id}'"

    # game/questmanager/engine/classes.rpy:36 "and state != "
    old "and state != "
    new "and state !="

    # game/questmanager/engine/classes.rpy:39 "Error: must be a tuple"
    old "Error: must be a tuple"
    new "Errore: deve essere una tupla"

    # game/questmanager/engine/classes.rpy:39 "hinata1"
    old "hinata1"
    new "hinata1"

    # game/questmanager/engine/classes.rpy:42 ", state="
    old ", state="
    new ", state="

    # game/questmanager/engine/classes.rpy:45 "Quest '{id}' title updated to: {new_title}"
    old "Quest '{id}' title updated to: {new_title}"
    new "Titolo della missione '{id}' aggiornato a: {new_title}"

    # game/questmanager/engine/classes.rpy:51 "\n[Sync Add] New quest '{quest_def.id}' found in definitions. Adding to manager."
    old "\n[Sync Add] New quest '{quest_def.id}' found in definitions. Adding to manager."
    new "\n[Sync Add] Nuova missione '{quest_def.id}' trovata nelle definizioni. Aggiunta al gestore."

    # game/questmanager/engine/classes.rpy:54 "\n--- Beginning attribute sync for all quests in manager... ---"
    old "\n--- Beginning attribute sync for all quests in manager... ---"
    new "\n--- Inizio della sincronizzazione degli attributi per tutte le missioni nel gestore... ---"

    # game/questmanager/engine/classes.rpy:57 "- Title is already in sync."
    old "- Title is already in sync."
    new "- Il titolo è già sincronizzato."

    # game/questmanager/engine/classes.rpy:66 "- Patching missing .wip attribute. Setting to Definition: {defined_wip}"
    old "- Patching missing .wip attribute. Setting to Definition: {defined_wip}"
    new "- Patching dell'attributo .wip mancante. Impostazione su Definizione: {defined_wip}"

    # game/questmanager/engine/classes.rpy:69 "[Sync] Source is a string. Collecting all definitions with base name: '{base_name}'..."
    old "[Sync] Source is a string. Collecting all definitions with base name: '{base_name}'..."
    new "[Sync] La sorgente è una stringa. Raccolta di tutte le definizioni con nome base: '{base_name}'..."

    # game/questmanager/engine/classes.rpy:81 "hinata2"
    old "hinata2"
    new "hinata2"

    # game/questmanager/engine/classes.rpy:87 "questlevel"
    old "questlevel"
    new "livellomissione"

    # game/questmanager/engine/classes.rpy:90 "- Syncing Quest Level: Saved={saved_level} -> Definition={defined_level}"
    old "- Syncing Quest Level: Saved={saved_level} -> Definition={defined_level}"
    new "- Sincronizzazione Livello Quest: Salvato={saved_level} -> Definizione={defined_level}"

    # game/questmanager/engine/classes.rpy:93 "- WARNING: Quest '{loaded_quest.id}' exists in save but has no definition in the script. Cannot synchronize."
    old "- WARNING: Quest '{loaded_quest.id}' exists in save but has no definition in the script. Cannot synchronize."
    new "- ATTENZIONE: La quest '{loaded_quest.id}' esiste nel salvataggio ma non ha una definizione nello script. Impossibile sincronizzare."

    # game/questmanager/engine/classes.rpy:96 "[Sync] Source is a tuple. Using it directly."
    old "[Sync] Source is a tuple. Using it directly."
    new "[Sync] La sorgente è una tupla. La uso direttamente."

    # game/questmanager/engine/classes.rpy:102 "category_name"
    old "category_name"
    new "category_name"

    # game/questmanager/engine/classes.rpy:105 "--- Manager.synchronize called with source: {source} ---"
    old "--- Manager.synchronize called with source: {source} ---"
    new "--- Manager.synchronize chiamato con sorgente: {source} ---"

