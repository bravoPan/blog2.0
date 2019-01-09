$(document).ready(function () {
    var images = $("body img");
    for (var i = 0; i < images.length; i++) {
        var index = images[i];
        var src = $(index).attr("src");
        var caption = $(index).attr("alt");
        var width = index.clientWidth;
        var height = index.clientHeight;
        $(index).attr("itemprop", "thumbnail");
        var gallery_node = document.createElement("a");
        $(gallery_node).attr("href", src).attr("itemprop", "contentUrl").attr("data-size", width + "x" + height);
        gallery_node.appendChild(index.cloneNode());

        //create figure caption
        var figure_caption = document.createElement("figcaption");
        $(figure_caption).attr("itemprop", "caption description");
        var description = document.createTextNode(caption);
        figure_caption.appendChild(description);

        //replace parent node
        var figure_item = document.createElement("figure");
        $(figure_item).attr("itemprop", "associatedMedia").attr("itemtype", "http://schema.org/ImageObject");
        figure_item.appendChild(gallery_node);
        figure_item.appendChild(figure_caption);

        $(index.parentNode).replaceWith(figure_item);
    }
});

