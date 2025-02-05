socket.on('gps_data', function(data) {
    console.log("Dados GPS recebidos:", data);

    // Verifica se os dados possuem latitude e longitude válidos
    if (data && data.latitude && data.longitude) {
        var lat = parseFloat(data.latitude);   // Garantir que é um número
        var lon = parseFloat(data.longitude);  // Garantir que é um número

        if (!isNaN(lat) && !isNaN(lon)) {
            // Atualiza a posição do marcador no mapa
            marker.setLatLng([lat, lon]);

            // Atualiza o centro do mapa (use setView para centralizar)
            map.setView([lat, lon], 13); // Centraliza o mapa com a nova posição
            console.log("Novo marcador posicionado em:", lat, lon);
        } else {
            console.error("Coordenadas inválidas recebidas:", data);
        }
    } else {
        console.error("Dados de GPS incompletos ou inválidos:", data);
    }
});
