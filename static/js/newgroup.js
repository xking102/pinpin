var React = require('react');


var injectTapEventPlugin = require("react-tap-event-plugin");
var mui = require('material-ui');
var ThemeManager = require('material-ui/lib/styles/theme-manager')();
var Colors = require('material-ui/lib/styles/colors');
var {Tabs, Tab, Paper} = mui;


injectTapEventPlugin();
var App = React.createClass({
  childContextTypes: {
    muiTheme: React.PropTypes.object
  },
  getChildContext: function() {
    return {
      muiTheme: ThemeManager.getCurrentTheme()
    };
  },
  listUser:function(){
    $.ajax({
      url      : '/api/v1/u/address',
      dataType : 'json',
      type     : 'post',
      contentType: "application/json",
      data:JSON.stringify({
                'isDefault':this.state.isDefault,
                'address_line1':this.state.address_line1,
                'address_line2':this.state.address_line2,
                'tel':this.state.tel,
                'reciver':this.state.reciver,
              }),
      success: function(resp) {
        console.log('succ');
      }.bind(this),

      error: function(xhr, status, err) {
        console.error(status, err.toString);
      }.bind(this)
    });
  },
  getInitialState:function(){
    return {
      title: '',
      desc: '',
      unit_price: 0,
      list_price: 0,
      total_req: 0,
      images:[],
      color:[],
      size:[],
      other:[]
    }
  },
  componentDidMount:function(){
    this.listUser();
    this.listAddress();
    ThemeManager.setPalette({
      accent1Color: Colors.blueGrey50
    });
  },
  onNewAddress:function( newAddress ){

    var newAddress = this.state.address.concat( newAddress );

    this.setState({
      address: newAddress,
    })
  },
  render: function () {
    return (
      <div>

          new group
        
      </div>
    );
  }
});




var mainCom = React.render(
  <App />,
  document.getElementById('app')
)

