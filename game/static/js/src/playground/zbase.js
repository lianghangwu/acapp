class AcGamePlayground{
    constructor(root) {
        this.root = root;
        this.$playground = $(`<div>Game Interface</div>`);
        
        this.hide();
        this.root.$ac_game.append(this.$playground);
        
        this.start();
    }

    start() {
        
    }

    show() { //show game interface
        this.$playground.show();
    }

    hide() { //close game interface
        this.$playground.hide();
    }
}
