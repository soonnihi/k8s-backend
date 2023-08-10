from core import models
import traceback
from django.http import JsonResponse

def insert_utils_board(
        board_seq=None,
        board_title=None,
        board_content=None,
        board_writer=None,
        board_password=None,
):
    try:
        if not board_title:
            return {
                'response_code': False,
                'message': '게시판 제목을 받지 못했습니다.'
            }
        if not board_content:
            return {
                'response_code': False,
                'message': '게시판 내용을 받지 못했습니다.'
            }
        if not board_writer:
            return {
                'response_code': False,
                'message': '게시판 작성자를 받지 못했습니다.'
            }
        if not board_password:
            return {
                'response_code': False,
                'message': '작성자 패스워드를 받지 못했습니다.'
            }
        if not board_seq:
            pass
        else:
            seq = None
            try:
                seq = models.TbBoard.objects.latest('board_seq').board_seq + 1
            except models.TbBoard.DoesNotExist:
                seq = 1
            tb_board = models.TbBoard()
            tb_board.board_seq = seq
            tb_board.board_title = board_title
            tb_board.board_content = board_content
            tb_board.board_writer = board_writer
            tb_board.board_password = board_password
            tb_board.save()
        return {
            'response_code': True,
            'message': '게시글이 저장되었습니다.'
        }
    except Exception:
        print(traceback.format_exc())
        return {
            'response_code': False,
            'message': '서버 에러'
        }

# rest
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

@csrf_exempt
def insert_board(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            result = insert_utils_board(
                board_title=data.get('board_title'),
                board_content=data.get('board_content'),
                board_writer=data.get('board_writer'),
                board_password=data.get('board_password'),
            )
            return JsonResponse(data=result, safe=False)
        except Exception as e:
            return JsonResponse(data={'response_code': False, 'message': '서버 에러'}, safe=False)
