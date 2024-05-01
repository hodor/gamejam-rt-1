import unreal

# Define the path to the Blueprint asset
blueprint_path = "/Game/Path/EntityPathSpawner.EntityPathSpawner"

# Load the Blueprint asset
entity_blueprint = unreal.load_asset(blueprint_path)

# Check if the blueprint is valid
if not entity_blueprint:
    raise ValueError("Blueprint not found at the specified path")

# Make sure it's the correct type
if not isinstance(entity_blueprint, unreal.Blueprint):
    raise TypeError("The asset at the path is not a Blueprint.")

# Get the Actor class from the blueprint's GeneratedClass
entity_blueprint_class = entity_blueprint.generated_class()

# Check if we successfully got the Actor class
if not entity_blueprint_class:
    raise Exception("Failed to get the Actor class from the Blueprint.")

# Get the current editor world using the Editor Utility Subsystem
editor_utility_subsystem = unreal.get_editor_subsystem(unreal.EditorUtilitySubsystem)
editor_world = editor_utility_subsystem.get_world()

# Spawn the actor in the world
spawned_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(entity_blueprint_class, unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0))

# Check if the actor was spawned successfully
if not spawned_actor:
    raise Exception("Failed to spawn actor")

# Find the spline component by class type
spline_component = unreal.SplineComponent(spawned_actor.get_component_by_class(unreal.SplineComponent.static_class()))

# Check if the spline component was found
if not spline_component:
    raise Exception("SplineComponent not found in the spawned actor")

# Modify the spline component as needed
# For example, adding points to the spline
spline_component.add_spline_point(unreal.Vector(100, 100, 0), unreal.SplineCoordinateSpace.WORLD)
spline_component.add_spline_point(unreal.Vector(200, 200, 0), unreal.SplineCoordinateSpace.WORLD)

# Update spline to see changes in the editor
spline_component.update_spline()

print("Spline has been modified with new points.")