import chess

# Piece positional values
pawntable = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]

knightstable = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]

bishopstable = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]

rookstable = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]

queenstable = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]

kingstable = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]


def gen_eval(board):
    """Evaluate board based on material and location"""
    evl=0
    
    if(board.is_checkmate()):
        if(board.turn):
            return 1000000
        else:
            return -1000000
        
    if(board.is_stalemate() or board.is_insufficient_material()):
        return 0
    
    white_pw=len(board.pieces(chess.PAWN,chess.WHITE))
    white_kn=len(board.pieces(chess.KNIGHT,chess.WHITE))
    white_bs=len(board.pieces(chess.BISHOP,chess.WHITE))
    white_rk=len(board.pieces(chess.ROOK,chess.WHITE))
    white_qn=len(board.pieces(chess.QUEEN,chess.WHITE))
    
    black_pw=len(board.pieces(chess.PAWN,chess.BLACK))
    black_kn=len(board.pieces(chess.KNIGHT,chess.BLACK))
    black_bs=len(board.pieces(chess.BISHOP,chess.BLACK))
    black_rk=len(board.pieces(chess.ROOK,chess.BLACK))
    black_qn=len(board.pieces(chess.QUEEN,chess.BLACK))
    
    material=1008*(white_pw-black_pw)+3191*(white_kn-black_kn)+3266*(white_bs-black_bs)+4961*(white_rk-black_rk)+9848*(white_qn-black_qn)
    
    pw_position_score=0
    for i in board.pieces(chess.PAWN,chess.WHITE):
        pw_position_score+=(pawntable[i]*10)        
    for i in board.pieces(chess.PAWN,chess.BLACK):
        pw_position_score-=(pawntable[chess.square_mirror(i)]*10)
        
    kn_position_score=0
    for i in board.pieces(chess.KNIGHT,chess.WHITE):
        kn_position_score+=(knightstable[i]*10)        
    for i in board.pieces(chess.KNIGHT,chess.BLACK):
        kn_position_score-=(knightstable[chess.square_mirror(i)]*10)
    
    bs_position_score=0
    for i in board.pieces(chess.BISHOP,chess.WHITE):
        bs_position_score+=(bishopstable[i]*10)        
    for i in board.pieces(chess.BISHOP,chess.BLACK):
        bs_position_score-=(bishopstable[chess.square_mirror(i)]*10)
    
    rk_position_score=0
    for i in board.pieces(chess.ROOK,chess.WHITE):
        rk_position_score+=(rookstable[i]*10)        
    for i in board.pieces(chess.ROOK,chess.BLACK):
        rk_position_score-=(rookstable[chess.square_mirror(i)]*10)
    
    qn_position_score=0
    for i in board.pieces(chess.QUEEN,chess.WHITE):
        qn_position_score+=(queenstable[i]*10)        
    for i in board.pieces(chess.QUEEN,chess.BLACK):
        qn_position_score-=(queenstable[chess.square_mirror(i)]*10)
    
    kg_position_score=0
    for i in board.pieces(chess.KING,chess.WHITE):
        kg_position_score+=(kingstable[i]*10)        
    for i in board.pieces(chess.KING,chess.BLACK):
        kg_position_score-=(kingstable[chess.square_mirror(i)]*10)
    
    evl=material+pw_position_score+kn_position_score+bs_position_score+rk_position_score+qn_position_score+kg_position_score
    
    if board.turn:
        return evl
    else:
        return -evl
    

def ab(board, a, b, dep):
    """Recursive Alpha-beta pruning search to given depth"""
    maximum=-1000001
    if(dep==0):
        return bottom(board, a, b)
    
    moves = order_moves(board, list(board.legal_moves))
    
    for m in moves:
        board.push(m)
        evl=-ab(board, -b, -a, dep-1)
        board.pop()
        if(evl>=b):
            return evl
        maximum=max(evl,maximum)
        a=max(a, evl)
    return maximum

def bottom(board, a, b):
    """Quiescence search - evaluate only capture moves to avoid horizon effect (high potential for blunders)"""
    evl=gen_eval(board)
    if(evl>=b):
        return b
    if(a<evl):
        a=evl
    for m in board.legal_moves:
        if board.is_capture(m):
            board.push(m)
            evl_bottom=-bottom(board, -b, -a)
            board.pop()

            if (evl_bottom>=b):
                return b
            if (evl_bottom>a):
                a=evl_bottom
    return a

def order_moves(board, moves):
    """Order moves for alpha-beta pruning efficiency (captures and checks first)"""
    def move_score(m):
        score = 0
        # Prioritize captures using MVV-LVA (Most Valuable Victim - Least Valuable Attacker)
        if board.is_capture(m):
            # MVV-LVA: Most Valuable Victim - Least Valuable Attacker
            victim = board.piece_at(m.to_square)
            attacker = board.piece_at(m.from_square)
            if victim and attacker:
                piece_values = {1: 100, 2: 320, 3: 330, 4: 500, 5: 900, 6: 20000}
                score += piece_values.get(victim.piece_type, 0) - piece_values.get(attacker.piece_type, 0)
        board.push(m)
        if board.is_check():
            score += 50
        board.pop()
        return score
    
    return sorted(moves, key=move_score, reverse=True)
        
def move(board, dep):
    """Find best move using alpha-beta pruning at specified depth"""
    best=chess.Move.null()
    maximum=-1000000
    a=-1000001
    b=1000001
    
    moves = order_moves(board, list(board.legal_moves))
    
    for m in moves:
        board.push(m)
        board_evl=-ab(board, -b, -a, dep-1)
        if(board_evl>maximum):
            maximum=board_evl 
            best=m
        board.pop()
    return best


def get_bot_move(fen_string, depth=3):
    """Check if game is over and get best move for black"""
    try:
        # Create board from FEN notation
        board = chess.Board(fen_string)

        if board.turn == chess.WHITE:
            return {
                "error": "It's White's turn, not Black's",
                "fen": fen_string
            }

        if board.is_game_over():
            result_reason = None
            if board.is_stalemate():
                result_reason = "stalemate"
            elif board.is_insufficient_material():
                result_reason = "insufficient_material"
            elif board.is_seventyfive_moves():
                result_reason = "seventyfive_moves"
            elif board.is_fivefold_repetition():
                result_reason = "fivefold_repetition"
            elif board.is_checkmate():
                result_reason = "checkmate"
            elif board.is_variant_draw():
                result_reason = "variant_draw"
            return {
                "error": "Game is already over",
                "fen": fen_string,
                "game_over": True,
                "result": board.result(),
                "result_reason": result_reason
            }
        
        best_move = move(board, depth)
        
        board.push(best_move)
        
        result_reason = None
        if board.is_game_over():
            if board.is_stalemate():
                result_reason = "stalemate"
            elif board.is_insufficient_material():
                result_reason = "insufficient_material"
            elif board.is_seventyfive_moves():
                result_reason = "seventyfive_moves"
            elif board.is_fivefold_repetition():
                result_reason = "fivefold_repetition"
            elif board.is_checkmate():
                result_reason = "checkmate"
            elif board.is_variant_draw():
                result_reason = "variant_draw"
        return {
            "fen": board.fen(),
            "move": best_move.uci(),
            "game_over": board.is_game_over(),
            "result": board.result() if board.is_game_over() else None,
            "result_reason": result_reason
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "fen": fen_string
        }
