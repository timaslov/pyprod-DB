<template>
  <div class="h-full rounded-lg container mx-10">

    <h1 class="text-xl text-center">
      Заголовок: {{ this.article.title }}
    </h1>

    <h1 class="text-xl text-center">
      Теги: {{ this.article.tags }}
    </h1>

    <h1 class="text-xl text-center">
      Родитель: {{ this.article.parent_id }}
    </h1>

    <h1 class="text-xl text-center">
      Слаг: {{ this.article.slug }}
    </h1>

    <div v-html="this.article.content" ></div>

    <button class="
                text-white
                bg-green-600
                hover:bg-green-800
                duration-300
                font-medium
                rounded-lg
                text-sm
                px-5
                py-2.5
                my-2
                mx-2
              "
    >
      Подтвердить
    </button>

    <button class="
                text-white
                bg-red-600
                hover:bg-red-800
                duration-300
                font-medium
                rounded-lg
                text-sm
                px-5
                py-2.5
              "
    >
      Отклонить
    </button>
  </div>
</template>

<script>
export default {
  name: "ArticleToApprove",
  data() {
    return {
      article:
          {title: "Article 6",
            id: "6",
            slug: "art6",
            parent_id: "1",
            tags: "tag1 tag2 tag3",
            content: "<div id=\"siteSub\" class=\"noprint\" style=\"font-size: 12.88px; color: #202122; font-family: sans-serif; background-color: #ffffff;\">Материал из Википедии &mdash; свободной энциклопедии</div>\n" +
                "<div id=\"contentSub\" style=\"font-size: 11.76px; line-height: 1.2em; margin: 0px 0px 1.4em 1em; color: #54595d; width: auto; font-family: sans-serif; background-color: #ffffff;\">\n" +
                "<div id=\"mw-content-subtitle\"></div>\n" +
                "</div>\n" +
                "<div id=\"contentSub2\" style=\"font-size: 11.76px; line-height: 1.2em; margin: 0px 0px 1.4em 1em; color: #54595d; width: auto; font-family: sans-serif; background-color: #ffffff;\"></div>\n" +
                "<div id=\"jump-to-nav\" style=\"color: #202122; font-family: sans-serif; font-size: 14px; background-color: #ffffff;\"></div>\n" +
                "<p><a class=\"mw-jump-link\" style=\"text-decoration-line: none; color: #0645ad; background: none #ffffff; display: block; clip: rect(1px, 1px, 1px, 1px); width: 1px; height: 1px; margin: -1px; border: 0px; padding: 0px; overflow: hidden; user-select: none; font-family: sans-serif; font-size: 14px; position: absolute !important;\" href=\"https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D1%82%D1%8C%D1%8F#mw-head\">Перейти к навигации</a><a class=\"mw-jump-link\" style=\"text-decoration-line: none; color: #0645ad; background: none #ffffff; display: block; clip: rect(1px, 1px, 1px, 1px); width: 1px; height: 1px; margin: -1px; border: 0px; padding: 0px; overflow: hidden; user-select: none; font-family: sans-serif; font-size: 14px; position: absolute !important;\" href=\"https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D1%82%D1%8C%D1%8F#searchInput\">Перейти к поиску</a></p>\n" +
                "<div id=\"mw-content-text\" class=\"mw-body-content mw-content-ltr\" dir=\"ltr\" lang=\"ru\" style=\"direction: ltr; color: #202122; font-family: sans-serif; font-size: 14px; background-color: #ffffff;\">\n" +
                "<div class=\"mw-parser-output\">\n" +
                "<table class=\"metadata plainlinks ts-Родственный_проект noprint ruwikiWikimediaNavigation\" style=\"font-size: 12.6px; background: #f8f9fa; border: 1px solid #a2a9b1; clear: right; float: right; margin: 0px 0px 1em 1em; padding: 0.4em; max-width: 19em; width: 19em; line-height: 1.5;\" role=\"presentation\">\n" +
                "<tbody>\n" +
                "<tr>\n" +
                "<th style=\"padding: 0.2em 0px; vertical-align: middle; width: 24px;\"><img class=\"noviewer\" style=\"border: 0px; vertical-align: middle;\" src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Notification-icon-Wiktionary-logo.svg/24px-Notification-icon-Wiktionary-logo.svg.png\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Notification-icon-Wiktionary-logo.svg/36px-Notification-icon-Wiktionary-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Notification-icon-Wiktionary-logo.svg/48px-Notification-icon-Wiktionary-logo.svg.png 2x\" alt=\"Логотип Викисловаря\" width=\"24\" height=\"24\" data-file-width=\"30\" data-file-height=\"30\" /></th>\n" +
                "<td style=\"padding: 0.2em 0px 0.2em 0.4em; vertical-align: middle;\">В&nbsp;<a style=\"text-decoration-line: none; color: #0645ad; background: none; overflow-wrap: break-word;\" title=\"Викисловарь\" href=\"https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C\">Викисловаре</a>&nbsp;есть статья &laquo;<span class=\"wikidict-ref\"><span style=\"font-weight: bold;\"><a class=\"extiw\" style=\"text-decoration-line: none; color: #3366bb; background: none; overflow-wrap: break-word;\" title=\"wikt:статья\" href=\"https://ru.wiktionary.org/wiki/%D1%81%D1%82%D0%B0%D1%82%D1%8C%D1%8F\">статья</a></span></span>&raquo;</td>\n" +
                "</tr>\n" +
                "</tbody>\n" +
                "</table>\n" +
                "<p style=\"margin: 0.5em 0px;\"><span style=\"font-weight: bold;\">Статья́</span>:</p>\n" +
                "<ul style=\"list-style-image: url('w/skins/Vector/resources/common/images/bullet-icon.svg?d4515'); margin: 0.3em 0px 0px 1.6em; padding: 0px;\">\n" +
                "<li style=\"margin-bottom: 0.1em;\"><a style=\"text-decoration-line: none; color: #0645ad; background: none; overflow-wrap: break-word;\" title=\"Статья (жанр журналистики)\" href=\"https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D1%82%D1%8C%D1%8F_(%D0%B6%D0%B0%D0%BD%D1%80_%D0%B6%D1%83%D1%80%D0%BD%D0%B0%D0%BB%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B8)\">Статья</a>&nbsp;в журналистике&nbsp;&mdash; один из основных жанров.</li>\n" +
                "<li style=\"margin-bottom: 0.1em;\"><a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0645ad; background: none; overflow-wrap: break-word;\" title=\"Научная статья\" href=\"https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D1%83%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D0%B0%D1%82%D1%8C%D1%8F\">Научная статья</a>&nbsp;&mdash; письменный опубликованный отчёт, описывающий итоги исследования.</li>\n" +
                "<li style=\"margin-bottom: 0.1em;\"><a style=\"text-decoration-line: none; color: #0645ad; background: none; overflow-wrap: break-word;\" title=\"Энциклопедическая статья\" href=\"https://ru.wikipedia.org/wiki/%D0%AD%D0%BD%D1%86%D0%B8%D0%BA%D0%BB%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D1%82%D0%B0%D1%82%D1%8C%D1%8F\">Энциклопедическая статья</a>&nbsp;&mdash; письменное описание чего-либо.</li>\n" +
                "<li style=\"margin-bottom: 0.1em;\"><a class=\"new\" style=\"text-decoration-line: none; color: #ba0000; background: none; overflow-wrap: break-word;\" title=\"Статья закона (страница отсутствует)\" href=\"https://ru.wikipedia.org/w/index.php?title=%D0%A1%D1%82%D0%B0%D1%82%D1%8C%D1%8F_%D0%B7%D0%B0%D0%BA%D0%BE%D0%BD%D0%B0&amp;action=edit&amp;redlink=1\">Статья</a>&nbsp;в юриспруденции&nbsp;&mdash; часть текста&nbsp;<a style=\"text-decoration-line: none; color: #0645ad; background: none; overflow-wrap: break-word;\" title=\"Закон (право)\" href=\"https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD_(%D0%BF%D1%80%D0%B0%D0%B2%D0%BE)\">закона</a>, закрепляющая юридические нормы.</li>\n" +
                "</ul>\n" +
                "</div>\n" +
                "</div>"
          }
    }
  },
}
</script>

<style scoped>

</style>