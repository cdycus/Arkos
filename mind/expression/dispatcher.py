from intents import Intent
from meta.alignment import check_alignment
from spine.router import dispatch_to_spine

class Dispatcher:
    def __init__(self, test_mode=False):
        self.test_mode = test_mode

    def dispatch(self, intent: Intent):
        if not check_alignment(intent.to_dict()):
            raise PermissionError("Intent not aligned with Skippy's purpose.")

        if self.test_mode:
            print("Dispatching intent:", intent.to_dict())
        else:
            dispatch_to_spine(intent.to_dict())
