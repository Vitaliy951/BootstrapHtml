from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PORT = 8000
BASE_DIR = Path(__file__).parent


class EmbeddedCSSHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == '/':
                # Загрузка HTML с встроенными стилями
                file_path = BASE_DIR / 'templates' / 'index.html'

                if not file_path.exists():
                    return self.send_error(404, "Файл index10.html не найден")

                with open(file_path, 'rb') as f:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "Страница не найдена")

        except Exception as e:
            self.send_error(500, f"Ошибка сервера: {str(e)}")


if __name__ == '__main__':
    with ThreadingHTTPServer(('', PORT), EmbeddedCSSHandler) as httpd:
        print(f"Сервер запущен на http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nСервер остановлен")
