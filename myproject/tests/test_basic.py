import pytest

pytestmark = pytest.mark.asyncio
# Используем асинхронный Playwright
@pytest.mark.asyncio
async def test_homepage_and_chart(page):
    # Открываем главную страницу
    response = await page.goto("http://localhost:8000/")
    assert response.status in [200, 404]  # Ожидаем ответ сервера

    # Проверяем API-страницу с графиком
    response = await page.goto("http://localhost:8000/api/participation_chart/")
    assert response.status == 200

    content = await page.content()
    assert "html" in content.lower()