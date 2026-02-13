import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from app.database import SessionLocal
from app.models import (
    Category, ViralPattern, TitleExample, ThumbnailCopy,
    DescriptionTemplate, Archetype, PowerVerb, TechnicalNoun,
    ContrastGap, EmotionalTrigger, ColorScheme, PlatformSyntax,
    ProductionWorkflow
)
import json

def seed():
    db = SessionLocal()
    try:
        # 1. CATEGORÍAS
        cat_racing = Category(
            name="RACING_TECH_OUTLIERS",
            description="Tecnología de competición con potencial outlier",
            niche_specialization=json.dumps({
                "visual_vocabulary": ["corte técnico", "flujo aerodinámico", "materiales expuestos"],
                "forbidden_cliches": ["llamas", "coches volando"]
            })
        )
        cat_performance = Category(name="PERFORMANCE_REVIEWS", description="Reviews de coches de altas prestaciones")
        cat_historical = Category(name="HISTORICAL_SECRETS", description="Secretos e historias no contadas de la automoción")
        cat_technical = Category(name="TECHNICAL_DEEP_DIVES", description="Análisis técnicos profundos")
        db.add_all([cat_racing, cat_performance, cat_historical, cat_technical])
        db.commit()

        # 2. PATRONES VIRALES (extraídos de Copy3.txt y Copy5.txt)
        pattern1 = ViralPattern(
            category_id=cat_racing.id,
            name="Tecnología Prohibida",
            pattern_template="El [Sistema/Componente] de [Marca] que fue BANEADO en [Tiempo] por [Razón Técnica]",
            psychological_triggers=json.dumps(["Controversia", "Tabú técnico", "Ingenio prohibido"]),
            ctr_range_min=18.0,
            ctr_range_max=30.0,
            avg_multiplier=18.5,
            success_rate=0.87,
            mining_evidence="Basado en 47 outliers similares",
            best_for="Tecnología de competición con controversia regulatoria"
        )
        pattern2 = ViralPattern(
            category_id=cat_historical.id,
            name="Secreto Histórico",
            pattern_template="El [Prototipo/Proyecto] de [Marca] que NUNCA Vio la Luz por [Razón]",
            psychological_triggers=json.dumps(["Misterio", "Historia oculta", "Qué pasaría si"]),
            ctr_range_min=16.0,
            ctr_range_max=26.0,
            avg_multiplier=16.2,
            success_rate=0.82,
            best_for="Historias de prototipos perdidos"
        )
        pattern3 = ViralPattern(
            category_id=cat_racing.id,
            name="Giant Slayer",
            pattern_template="Cómo [Underdog] DESTROZÓ a [Gigante] en [Competición]",
            psychological_triggers=json.dumps(["Underdog", "Justicia", "Humillación"]),
            ctr_range_min=17.0,
            ctr_range_max=28.0,
            avg_multiplier=17.3,
            success_rate=0.84,
            best_for="Historias de underdogs"
        )
        db.add_all([pattern1, pattern2, pattern3])
        db.commit()

        # 3. EJEMPLOS DE TÍTULOS
        ex1 = TitleExample(
            viral_pattern_id=pattern1.id,
            title_text="El Sistema de Suspensión Hidráulica de Williams que Fue Prohibido por Ser Demasiado Inteligente (1993)",
            ctr_estimate=24.5,
            emotional_triggers=json.dumps(["Controversia", "Admiración"]),
            technical_specs=json.dumps(["suspensión hidráulica", "Williams FW15C"]),
            source_channel="Chain Bear"
        )
        ex2 = TitleExample(
            viral_pattern_id=pattern2.id,
            title_text="El Hypercar de Yamaha que Podría Haber Cambiado Todo (Proyecto OX99-11, 1992)",
            ctr_estimate=22.1,
            emotional_triggers=json.dumps(["Nostalgia", "Misterio"]),
            technical_specs=json.dumps(["OX99-11", "V12", "3.5L"]),
            source_channel="Donut Media"
        )
        db.add_all([ex1, ex2])
        db.commit()

        # 4. COPIAS DE MINIATURAS
        thumb1 = ThumbnailCopy(
            category_id=cat_racing.id,
            text="BANNED TECH",
            placement="Top-Right",
            color_scheme="Yellow/Black/Red",
            readability_score=9.8,
            best_for="Tecnología prohibida"
        )
        thumb2 = ThumbnailCopy(
            category_id=cat_performance.id,
            text="REVIEW COMPLETA",
            placement="Top-Left",
            color_scheme="White/Red",
            readability_score=9.5,
            best_for="Reviews de coches"
        )
        thumb3 = ThumbnailCopy(
            category_id=cat_racing.id,
            text="510 HP",
            placement="Bottom-Left",
            color_scheme="Yellow/Black",
            readability_score=9.9,
            best_for="Especificaciones de potencia"
        )
        db.add_all([thumb1, thumb2, thumb3])
        db.commit()

        # 5. PLANTILLAS DE DESCRIPCIÓN
        desc1 = DescriptionTemplate(
            category_id=cat_racing.id,
            name="Outlier Report",
            template_text=(
                "📊 **REPORTE OUTLIER** - Este video analiza un outlier detectado en nuestra minería de 10,000+ videos.\n\n"
                "• **Dataset analizado:** {dataset} videos en nicho {niche}\n"
                "• **Patrón viral:** {pattern} (success rate: {success_rate}%)\n"
                "• **Multiplicador esperado:** {multiplier}x promedio del canal\n\n"
                "⏱️ **CAPÍTULOS:**\n{chapters}\n\n"
                "🔧 **EQUIPO UTILIZADO:**\n{equipment}\n\n"
                "💬 **¿QUÉ OPINAS?** {cta}\n\n"
                "#hashtags"
            ),
            retention_boost=48.0,
            sections=json.dumps(["Hook", "DataProof", "Chapters", "Equipment", "CTA", "Hashtags"])
        )
        db.add(desc1)
        db.commit()

        # 6. ARQUETIPOS
        arch1 = Archetype(
            name="FORBIDDEN_FRUIT",
            emotional_trigger="Curiosity & Authority Challenge",
            syntax_template="The [Adjective] Car that [Authority] Tried to Hide/Ban",
            power_verbs=json.dumps(["Banned", "Hidden", "Censored", "Erased"]),
            amplifiers=json.dumps(["Secretly", "Illegally", "Forever"])
        )
        arch2 = Archetype(
            name="GIANT_SLAYER",
            emotional_trigger="Justice & Underdog Bias",
            syntax_template="How [Underdog] Humiliated/Destroyed [Giant]",
            power_verbs=json.dumps(["Humiliated", "Destroyed", "Massacred", "Crushed"]),
            amplifiers=json.dumps(["Instantly", "Brutally", "Completely"])
        )
        db.add_all([arch1, arch2])
        db.commit()

        # 7. VERBOS DE PODER
        verbs = [
            PowerVerb(verb="DESTROZÓ", intensity=10, category="automotive"),
            PowerVerb(verb="HUMILLÓ", intensity=9, category="automotive"),
            PowerVerb(verb="BANEÓ", intensity=9, category="automotive"),
            PowerVerb(verb="REVOLUCIONÓ", intensity=8, category="automotive"),
        ]
        db.add_all(verbs)
        db.commit()

        # 8. SUSTANTIVOS TÉCNICOS
        nouns = [
            TechnicalNoun(noun="MOTOR"),
            TechnicalNoun(noun="AERODINÁMICA"),
            TechnicalNoun(noun="CHASIS"),
            TechnicalNoun(noun="TURBO"),
        ]
        db.add_all(nouns)
        db.commit()

        # 9. GAPS DE CONTRASTE
        gaps = [
            ContrastGap(gap_text="PEQUEÑO vs GIGANTE"),
            ContrastGap(gap_text="BARATO vs CARO"),
            ContrastGap(gap_text="LENTO vs RÁPIDO"),
        ]
        db.add_all(gaps)
        db.commit()

        # 10. TRIGGERS EMOCIONALES
        triggers = [
            EmotionalTrigger(name="Curiosity Gap", potency=95),
            EmotionalTrigger(name="Social Proof", potency=92),
            EmotionalTrigger(name="Controversy", potency=88),
            EmotionalTrigger(name="Urgency", potency=90),
        ]
        db.add_all(triggers)
        db.commit()

        # 11. ESQUEMAS DE COLOR
        colors = [
            ColorScheme(name="Peligro/Urgencia", primary_color="Red", secondary_color="Black", emotion="Danger/Urgency", placement_priority="Top-Right", performance_boost=25.0),
            ColorScheme(name="Tecnología", primary_color="Cyan", secondary_color="Black", emotion="Future/Tech", placement_priority="Bottom-Left", performance_boost=18.0),
        ]
        db.add_all(colors)
        db.commit()

        # 12. SINTAXIS POR PLATAFORMA IA
        platforms = [
            PlatformSyntax(
                platform_name="Midjourney",
                syntax_template="/imagine prompt: [Subject] + [Environment] + [Lighting/Mood] + [Camera/Lens] --ar 16:9 --stylize 250 --v 6.0 --style raw",
                forbidden_words=json.dumps(["text in image", "HDR", "4k", "8k"]),
                notes="Usar --iw 2.0 si hay imagen de referencia"
            ),
            PlatformSyntax(
                platform_name="DALL-E 3",
                syntax_template="Detailed descriptive paragraph focusing on literal visual elements + 'The text \"[TEXT]\" is clearly visible in [font style]'.",
                forbidden_words=json.dumps([]),
                notes="Usar lenguaje natural, evitar jerga técnica"
            ),
        ]
        db.add_all(platforms)
        db.commit()

        # 13. FLUJO DE PRODUCCIÓN PREDEFINIDO
        workflow_steps = [
            {"id": "extract_script", "name": "Extracción de ADN del guión", "required_inputs": ["script"], "next": {"default": "generate_titles"}},
            {"id": "generate_titles", "name": "Generación de títulos", "required_inputs": ["topic", "emotion", "technical_level"], "next": {"default": "select_title"}},
            {"id": "select_title", "name": "Selección de título por el usuario", "required_inputs": ["title_id"], "next": {"default": "generate_thumbnail_copy"}},
            {"id": "generate_thumbnail_copy", "name": "Generación de copias para miniatura", "required_inputs": ["title_id", "category"], "next": {"default": "select_thumbnail_copy"}},
            {"id": "select_thumbnail_copy", "name": "Selección de copy por el usuario", "required_inputs": ["thumbnail_copy_id"], "next": {"has_reference_image": "generate_image_with_reference", "default": "generate_image_direct"}},
            {"id": "generate_image_with_reference", "name": "Generar prompt con referencia visual", "required_inputs": ["reference_image", "thumbnail_copy_id", "title_id"], "next": {"default": "generate_seo"}},
            {"id": "generate_image_direct", "name": "Generar prompt directo", "required_inputs": ["thumbnail_copy_id", "title_id"], "next": {"default": "generate_seo"}},
            {"id": "generate_seo", "name": "Generar descripción SEO y tags", "required_inputs": ["title_id", "thumbnail_copy_id", "script_metadata"], "next": {"default": "complete"}},
            {"id": "complete", "name": "Flujo completado", "required_inputs": [], "next": {}}
        ]
        workflow = ProductionWorkflow(
            name="Flujo Estándar OEMB",
            description="Flujo de producción con rama de referencia visual opcional",
            steps=json.dumps(workflow_steps)
        )
        db.add(workflow)
        db.commit()

        print("✅ Base de datos inicializada con datos de ejemplo.")
    finally:
        db.close()

if __name__ == "__main__":
    seed()