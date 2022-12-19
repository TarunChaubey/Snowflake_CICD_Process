from src.helper_function import create_session_object

session = create_session_object()

print(session.sql('show database'))