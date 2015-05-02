var React = require("react");

var Message = React.createClass({
    render : function(){
        var msg = this.props.message;
        return(
            <div>
                <h3>{msg.email}&nbsp;&nbsp;
                    <small>{msg.id}</small>
                </h3>
                <p>{msg.nickname}</p>
            </div>
        )
    }
});

module.exports = Message;