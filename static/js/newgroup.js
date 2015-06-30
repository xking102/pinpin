var React = require('react');


var injectTapEventPlugin = require("react-tap-event-plugin");
var mui = require('material-ui');
var ThemeManager = require('material-ui/lib/styles/theme-manager')();
var Colors = require('material-ui/lib/styles/colors');
var {TextField, Paper, RaisedButton} = mui;
var Dropzone = require('react-dropzone');


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
  PostGroup:function(){
    var formData = new FormData();
    for (var i=0;i<this.state.images.length;i++){
      var file = this.state.images[i];
      console.log(file);
      formData.append('photos',file);
    }
    formData.append('images',this.state.images);
    formData.append('title',this.refs.title.getValue());
    formData.append('desc',this.refs.desc.getValue());
    formData.append('unit_price',this.refs.price.getValue());
    formData.append('list_price',0);
    formData.append('total_qty',this.refs.qty.getValue());
    $.ajax({
      url      : '/api/v1/groups',
      type     : 'POST',
      dataType: 'json',
      cache: false,
      contentType: false,
      processData: false,
      data:formData,
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
      images:[],
      color:[],
      size:[],
      other:[],
      flag:true
    }
  },
  onNewAddress:function( newAddress ){

    var newAddress = this.state.address.concat( newAddress );

    this.setState({
      address: newAddress,
    })
  },
  _handleForm:function(e){
    e.preventDefault();
    this.PostGroup();
  },
  render: function () {
    return (
      <div style={{marginLeft:'24%',marginRight:'27%'}}  >
          <Paper zDepth={3}>
          <div style={{marginLeft:'10px',marginRight:'10px',paddingBottom:'20px'}}>



          <form onSubmit={this._handleForm} ref="addGroupForm" name="addGroup" encType="multipart/form-data" method="POST">
            <TextField
              ref="title"
              style={{width:'550px'}}
              hintText="商品名称"
              type='text'
              multiLine={true}
              floatingLabelText="输入商品名称"
            />

            <br/>

            <TextField
              ref="desc"
              style={{width:'550px'}}
              hintText="商品详情介绍"
              type='text'
              multiLine={true}
              floatingLabelText="输入商品详情介绍"
            />

            <br/>

            <TextField
              ref="price"
              hintText="到手单价"
              floatingLabelText="输入到手单价"
              errorText={this.state.errorPrice}
              onChange={this._handleErrorPrice}
            />



            <TextField
              ref="qty"
              hintText="团购数量"
              floatingLabelText="输入本次团购数量"
              errorText={this.state.errorQty}
              onChange={this._handleErrorQty}
            />

            <br/>
            <br/>
            <br/>

            <Dropzone ref="dropzone" onDrop={this._onDrop} size={150} >
              <div>你可以拖拽多张图片到此处或者双击选择多张图片</div>
            </Dropzone>
            {this.showFiles()}

            <br/>


            <div className="pull-right">
            <a className="btn btn-link" onClick={this._onHandleCancel}>重新填写</a>
            &nbsp;
            <RaisedButton
            label="添加"
                secondary={true}
            />
            </div>



          </form>


          </div>
          </Paper>

      </div>
    );
  },

  _onDrop:function(imgs){
    this.setState({
      images:imgs
    });
  },

  showFiles: function () {
    if (this.state.images.length <= 0) {
      return '';
    }

    var images = this.state.images;

    return (
      <div>
        <h3>预览</h3>
          {[].map.call(images, function (f, i) {
            return <img style={{marginRight:'5px'}}width={100} height={100} key={i} src={f.preview} />;
          })}
      </div>
    );
  },



  _onHandleCancel:function(){
    this.refs.addGroupForm.getDOMNode().reset();
  },

  _handleErrorPrice:function(){
    if(this.refs.price.getValue()>0){
      this.setState({
        errorPrice:''
      });
    }else{
      this.setState({
        errorPrice:'请输入大于0的数字'
      })
    }
  },


  _handleErrorQty:function(){
    var num = this.refs.qty.getValue();
    if(num>0&&num%1==0){
      this.setState({
        errorQty:''
      });
    }else{
      this.setState({
        errorQty:'请输入大于0的整数'
      })
    }
  },

});




var mainCom = React.render(
  <App />,
  document.getElementById('app')
)

