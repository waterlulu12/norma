from _typeshed import Self
from typing import Optional, List, Any, Tuple


class Baghchal:
    def __new__(
        cls: type[Self],
        turn: Optional[int] = None,
        goat_counter: Optional[int] = None,
        goat_captured: Optional[int] = None,
        game_state: Optional[Any] = None,
        game_history: Optional[List[Any]] = None,
        pgn: Optional[str] = None,
        prev_move: Optional[Any] = None,
        move_reward_tiger: Optional[List[float]] = None,
        move_reward_goat: Optional[List[float]] = None,
        trapped_tiger: Optional[int] = None,
    ) -> Self:
        ...

    @staticmethod
    def default() -> Baghchal:
        ...

    @staticmethod
    def from_str(serialized: str) -> Baghchal:
        ...

    @staticmethod
    def pgn_unit_to_coord(pgn: str) -> Tuple[Optional[List[int]], List[int]]:
        ...

    @staticmethod
    def coord_to_png_unit(destination: List[int], source: Optional[List[int]]) -> str:
        ...

    @staticmethod
    def i2m_goat(index: int) -> Tuple[Optional[List[int]], List[int]]:
        ...

    @staticmethod
    def i2m_placement(index: int) -> Tuple[Optional[List[int]], List[int]]:
        ...

    @staticmethod
    def i2m_tiger(index: int) -> Tuple[Optional[List[int]], List[int]]:
        ...

    @staticmethod
    def m2i_goat(__move__: Tuple[Optional[List[int]], List[int]]) -> int:
        ...

    @staticmethod
    def m2i_placement(__move__: Tuple[Optional[List[int]], List[int]]) -> int:
        ...

    @staticmethod
    def m2i_tiger(__move__: Tuple[Optional[List[int]], List[int]]) -> int:
        ...

    def index_to_input(self, index: int, symmetry: int) -> List[List[int]]:
        ...

    def set_rewards(
        self,
        t_goat_capture,
        t_got_trapped,
        t_trap_escape,
        t_win,
        t_lose,
        t_draw,
        t_move,
        g_goat_captured,
        g_tiger_trap,
        g_tiger_escape,
        g_win,
        g_lose,
        g_draw,
        g_move,
        gt_invalid_move,
    ):
        ...

    def merged_rewards(self) -> List[float]:
        ...

    def copy(self) -> Baghchal:
        ...

    def to_str(self) -> str:
        ...

    def set_game_over_on_invalid(self, state: bool):
        ...

    def board(self) -> List[List[int]]:
        ...

    def move_count(self) -> int:
        ...

    def game_status_check(self) -> GameStatusCheckResult:
        ...

    def turn(self) -> int:
        ...

    def goat_counter(self) -> int:
        ...

    def goat_captured(self) -> int:
        ...

    def game_state(self) -> GameStatus:
        ...

    def game_history(self) -> List[GameStateInstance]:
        ...

    def pgn(self) -> str:
        ...

    def prev_move(self) -> Optional[Tuple[Optional[List[int]], List[int]]]:
        ...

    def move_reward_tiger(self) -> List[float]:
        ...

    def trapped_tiger(self) -> int:
        ...

    def move_reward_goat(self) -> List[float]:
        ...

    def make_move_index(self, index: int) -> Optional[TransitionHistoryInstance]:
        ...

    def state_as_inputs(
        self,
        mode: int,
        rotate_board: Optional[bool] = False,
        possible_moves_pre: Optional[List[PossibleMove]] = None,
    ) -> List[List[int]]:
        ...

    def state_as_inputs_all_symmetry(
        self,
        possible_moves_pre: Optional[List[PossibleMove]] = None,
    ) -> List[List[List[int]]]:
        ...

    def transition_history(self) -> List[TransitionHistoryInstance]:
        ...

    def state_as_input_actor(
        self,
        mode: int,
        rotate_board: Optional[bool] = False,
        possible_moves_pre: Optional[List[PossibleMove]] = None,
    ) -> List[int]:
        ...

    def clear_game(self) -> None:
        ...

    def resign(self, side) -> GameStatusCheckResult:
        ...

    def load_game(self, pgn: str) -> None:
        ...

    def make_move(
        self,
        target: List[int],
        source: Optional[List[int]],
        eval_res: Optional[MoveCheckResult],
    ) -> MoveCheckResult:
        ...

    def make_move_with_symmetry(
        self,
        target: List[int],
        source: Optional[List[int]],
        symmetry: int,
    ) -> MoveCheckResult:
        ...

    def get_possible_moves(self) -> List[PossibleMove]:
        ...


class GameStatus:
    NotDecided: Any
    GoatWon: Any
    TigerWon: Any
    Draw: Any

    def to_value(self) -> int:
        ...

    @staticmethod
    def from_value(value: int) -> GameStatus:
        ...


class PossibleMove:
    move: Tuple[Optional[List[int]], List[int]]
    resulting_state: Baghchal

    def to_str(self) -> str:
        ...


class MoveCheckResult:
    is_valid: bool
    is_place_move: bool
    is_capture_move: bool
    capture_piece: Optional[List[int]]
    reason: str

    def to_str(self) -> str:
        ...


class GameStatusCheckResult:
    decided: bool
    won_by: int

    def to_str(self) -> str:
        ...


class GameStateInstance:
    board: List[List[int]]
    goat_count: int
    goat_captured: int

    def to_str(self) -> str:
        ...


class TransitionHistoryInstance:
    move: Tuple[Optional[List[int]], List[int]]
    state: List[List[List[int]]]
    resulting_state: List[List[List[int]]]
    move_reward: float
    is_terminal: bool
    transition_type: MoveType

    def move_index(self) -> int:
        ...

    def move_vector(self) -> List[int]:
        ...


class MoveType:
    TigerMove: Any
    GoatMove: Any
    GoatPlacement: Any
