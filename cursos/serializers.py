from rest_framework import serializers

from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = [
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        ]
    
    def validate_avaliacao(self, attrs):
        if attrs in range(1, 11):
            return True
        raise serializers.ValidationError('A avaliação deve ser um inteiro entre 1 e 10')


class CursoSerializer(serializers.ModelSerializer):
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        ]