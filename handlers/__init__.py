from aiogram import Router, F




def setup_routers() -> Router:

    from handlers import start_command, support, statistics
    from callbacks import (contacts_and_menu, main_menu_callback, contacts,
        thanks_callback, want_to_participate, success_story)
    
    from callbacks.first_layer_menu import (about_callback, criteries_callback, results,
        calendar_text, steps_callback)
    
    
    router = Router()
    # router.include_router(help_command.router)
    router.include_router(start_command.router)
    router.include_router(about_callback.router)
    router.include_router(criteries_callback.router)
    router.include_router(results.router)
    router.include_router(calendar_text.router)
    router.include_router(steps_callback.router)
    router.include_router(contacts_and_menu.router)
    router.include_router(main_menu_callback.router)
    router.include_router(contacts.router)
    router.include_router(thanks_callback.router)
    router.include_router(want_to_participate.router)
    router.include_router(success_story.router)
    router.include_router(support.router)
    router.include_router(statistics.router)
    
    

    
    

    return router