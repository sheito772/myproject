$(document).ready(function() {
    let index = 0;
    let intervlId = null;
    let typingSpeed = 40;
    let isTyping = false;
    let story = [
        {text: "かつて、遥か彼方の宇宙に、ひとつの美しい星がありました。", image: "/static/images/default_image.jpg"},
        {text: "そこには、様々な生命が共存し、平和な時代が続いていました。", image: "/static/images/default_image.jpg"},
        {text: "しかし、ある日、暗黒の力が星を覆い始めました。", image: "/static/images/dark_image.jpg"},
        {text: "暗黒の力は、星の生命たちを次々と闇へと変えていきました。", image: "/static/images/dark_image.jpg"},
        {text: "星の生命たちが絶望する中、一筋の光が現れました。", image: "/static/images/light_image.jpg"},
        {text: "それは、星の守護神が遣わしたとされる、勇者の光でした。", image: "/static/images/light_image.jpg"},
        {text: "勇者は、星を救うため、一人で暗黒の力に立ち向かう決意をしました。", image: "/static/images/hero_image.jpg"},
        {text: "長い戦いが続き、勇者は何度も傷つきながらも、決して諦めませんでした。", image: "/static/images/hero_image.jpg"},
        {text: "そしてついに、勇者は暗黒の力を封じ、星に平和を取り戻しました。", image: "/static/images/peace_image.jpg"},
        {text: "それ以降、星の生命たちは勇者を祝福し、平和な時代が再び訪れました。", image: "/static/images/peace_image.jpg"}
    ];

    function typeWriter(text,callback) {
        let i = 0;
        isTyping = true;
        intervlId = setInterval(function() {
            $("#text").append(text.charAt(i));
            i++;
            if (i === text.length) {
                clearInterval(intervlId);
                isTyping = false;
                typingSpeed = 40;
                callback();
            }
        }, typingSpeed);
    }

    function loadStory() {
        clearInterval(intervlId);
        $("#text").empty();
        typeWriter(story[index].text, function() {});
        $("#image").attr('src', story[index].image);
        index++;
        if (index === story.length) {
            index = 0;
        };
    }

    $('#banner').click(function() {
        console.log("Banner clicked!");
        if (isTyping) {
            console.log("Typing... speeding up.");
            clearInterval(intervalId);
            typingSpeed /= 4;
            typeWriter(story[index + 1].text.slice($("#text").text().length), function() {});
          } else {
            console.log("Loading next story...");
            loadStory();
        }
    })

    $(document).addEventListener('keydown', function (e) {
        if(e.key === 'r' || e.key === 'R'){
            window.location.reload();
        }
    });
})