var React = require("react");
var mui = require('material-ui');
var {Paper} = mui;

module.exports = React.createClass({

    contextTypes: {
        router: React.PropTypes.func.isRequired
    },
    getInitialState:function(){
      if (this.props.addr.isDefault){
        var addId = this.props.addr.id;
        this.props.setCurrentAddress(addId);
        console.log(addId);
      }
      return {
        address:[],
     }
    },
    handlerSetAddress: function(){
      
      var addId = this.props.addr.id;
      this.props.setCurrentAddress(addId);
      console.log(addId);
    },
    render:function(){
       
    return(
                <div className="row-fluid">
                    
                    <div className="span2">{this.props.addr.reciver}</div>
                    <div className="span6">{this.props.addr.address_line1}</div>
                    <div className="span2">{this.props.addr.tel}</div>
                    <div className="span2">
                        <a className="btn btn-link" href="javascript:void(0)" onClick={this.handlerSetAddress}>使用本地址</a>
                    </div>
                </div>

    )   
  }
})